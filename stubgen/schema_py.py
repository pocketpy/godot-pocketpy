from dataclasses import dataclass, field
from enum import Enum
from functools import cached_property
import re
from typing import ClassVar, Literal, override


from .tools import validate_types_on_init, ValidatorResults, DEBUG, build_dependency_graph, topological_sort
from .schema_gdt import GodotInOne
from keyword import iskeyword
import traceback




class PyTypeCategory(Enum):
    CAN_TRANSFER_TO_PY_BUILTIN = "CAN_TRANSFER_TO_PY_BUILTIN"
    GODOT_NATIVE = "GODOT_NATIVE"
    ENUM = "ENUM"
    SINGLETON_GODOT_NATIVE = "SINGLETON_GODOT_NATIVE"
    IGNORE = "IGNORE"





@validate_types_on_init
@dataclass
class PyType:  # MARK: PyType 
    '''
    一个python原子类型
    '''
    
    
    # src\lang\Common.cpp
    #
    # Variant py_tovariant(py_Ref val) {
    # 	switch (py_typeof(val)) {
    # 		case tp_NoneType:
    # 			return Variant();
    # 		case tp_bool:
    # 			return py_tobool(val);
    # 		case tp_int:
    # 			return py_toint(val);
    # 		case tp_float:
    # 			return py_tofloat(val);
    # 		case tp_str: {
    # 			c11_sv sv = py_tosv(val);
    # 			return String::utf8(sv.data, sv.size);
    # 		}
    # 		default: {
    # 			if (py_istype(val, pyctx()->tp_Variant)) {
    # 				void *ud = py_touserdata(val);
    # 				return *static_cast<Variant *>(ud);
    # 			} else {
    # 				return {};
    # 			}
    # 		}
    # 	}
    # }
    name: str
        
    COMPATIBLE_TYPES_MAP: ClassVar[dict[str, str]] = {"Nil":'None', "int":'int', "float":'float', "bool":'bool', "String":'str'}    
    
    ALL_TYPES: ClassVar[dict[str, 'PyType']] = {}
    
    
    # Type categorization sets
    COMPATIBLE_TYPES: ClassVar[set['PyType']] = set()
    GODOT_NATIVE_TYPES: ClassVar[set['PyType']] = set()
    ENUM_TYPES: ClassVar[set['PyType']] = set()
    SINGLETON_GODOT_NATIVE_TYPES: ClassVar[set['PyType']] = set()
    IGNORE_TYPES: ClassVar[set['PyType']] = set()
    # 支持泛型的类型
    SUPPORT_GENERIC_TYPES: ClassVar[set['PyType']] = set()
    
    # 子类查找缓存
    _SUBCLASSES_CACHE: ClassVar[dict[str, list['PyType']]] = {}
    
    inherit: 'PyType | None' = field(default=None)
    
    @override
    def __hash__(self) -> int:
        return hash(self.name)
    
    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PyType):
            return False
        return self.name == other.name
    
    @classmethod
    def get(cls, name: str) -> 'PyType':
        result = cls._get(name, raise_error=True)
        if result is None:
            raise ValueError(f"Type not found: {name}")
        return result
    
    @classmethod
    def try_get(cls, name: str) -> 'PyType | None':
        return cls._get(name, raise_error=False)
    
    @classmethod
    def _get(cls, name: str, raise_error: bool = True) -> 'PyType | None':
        '''
        根据名字获取PyType, 设计时只允许用来获取原子类型
        '''
        name = PyType.parse_name(name)
        if name not in PyType.ALL_TYPES:
            if raise_error:
                # 按首字母分组打印类型名
                type_names = sorted(PyType.ALL_TYPES.keys())
                grouped_types = {}
                for type_name in type_names:
                    first_letter = type_name[0].upper()
                    if first_letter not in grouped_types:
                        grouped_types[first_letter] = []
                    grouped_types[first_letter].append(type_name)
                
                error_msg = f"Type not found: {name}\n\tALL_TYPES:\n"
                for letter in sorted(grouped_types.keys()):
                    error_msg += f"\t{letter}: {', '.join(grouped_types[letter])}\n"
                
                raise ValueError(error_msg.rstrip())
            return None
        pytype = PyType.ALL_TYPES[name]
        return pytype
    
    @classmethod
    def add(cls, name: str, category: PyTypeCategory) -> None:
        '''
        添加一个PyType, 此处为系统收录类型的唯一门户, 注意保证name的干净
        '''
        name = PyType.parse_name(name)
        new_pytype = PyType(name=name)
        if not PyType.validate(new_pytype):
            raise ValueError(f"Invalid type: {name}")
        
        cls.ALL_TYPES[name] = new_pytype
        
        # 强制识别并添加内置类型, 而不是将内置类型传入期望的类别
        if name in cls.COMPATIBLE_TYPES_MAP or name in cls.COMPATIBLE_TYPES_MAP.values():
            cls.add_type_to_category(new_pytype, PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN)
        else:
            cls.add_type_to_category(new_pytype, category)
    
    @classmethod
    def add_type_to_category(cls, pytype: 'PyType', category: PyTypeCategory) -> None:
        """
        将一个PyType添加到指定的类别集合中
        """
        if category == PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN:
            cls.COMPATIBLE_TYPES.add(pytype)
        elif category == PyTypeCategory.GODOT_NATIVE:
            cls.GODOT_NATIVE_TYPES.add(pytype)
        elif category == PyTypeCategory.ENUM:
            cls.ENUM_TYPES.add(pytype)
        elif category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
            cls.SINGLETON_GODOT_NATIVE_TYPES.add(pytype)
        elif category == PyTypeCategory.IGNORE:
            cls.IGNORE_TYPES.add(pytype)
        else:
            raise ValueError(f"Invalid category: {category}")
        
    
    @classmethod
    def get_subclasses(cls, base_type: 'PyType') -> list['PyType']:
        '''
        返回所有继承自 base_type 的 PyType 列表
        '''
        # 检查缓存中是否已有结果
        if base_type.name in cls._SUBCLASSES_CACHE:
            return cls._SUBCLASSES_CACHE[base_type.name]
            
        subclasses = []
        
        # 直接子类
        direct_subclasses = [t for t in cls.ALL_TYPES.values() if t.inherit == base_type]
        
        # 递归查找所有子类
        for subclass in direct_subclasses:
            subclasses.append(subclass)
            # 递归获取子类的子类
            subclasses.extend(cls.get_subclasses(subclass))
        
        # 将结果存入缓存
        cls._SUBCLASSES_CACHE[base_type.name] = subclasses
        
        return subclasses
        
    @classmethod
    def build_type_sets(cls, gdt_all_in_one: GodotInOne) -> None:
        '''
        从gdt_all_in_one构建PyType.ALL_TYPES
        '''
        # 支持泛型的类型
        for name in ['Array']:
            cls.ALL_TYPES[name] = PyType(name=name)
            cls.SUPPORT_GENERIC_TYPES.add(cls.get(name))
        
        # Variant
        cls.add('Variant', PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN)
        
        # intptr
        cls.add('intptr', PyTypeCategory.IGNORE)
        
        # Enum
        cls.add('Enum', PyTypeCategory.IGNORE)
        
        # 单例类型
        for singleton_data in gdt_all_in_one.singletons:
            cls.add(singleton_data.name, PyTypeCategory.SINGLETON_GODOT_NATIVE)
        
        # 内置类型
        for builtin_class in gdt_all_in_one.builtin_classes:
            cls.add(builtin_class.name, PyTypeCategory.GODOT_NATIVE)
        
        # 枚举和内置
        for cls_data in gdt_all_in_one.classes:
            
            cls.add(cls_data.name, PyTypeCategory.GODOT_NATIVE)
            
            if cls_data.enums:
                for enum_data in cls_data.enums:
                    name = cls_data.name + '__' + enum_data.name
                    cls.add(name, PyTypeCategory.ENUM)
                    cls.get(name).inherit = cls.get("Enum")
                    
            cls.add(cls_data.name, PyTypeCategory.GODOT_NATIVE)
        
        
        for builtin_cls_data in gdt_all_in_one.builtin_classes:
            if builtin_cls_data.enums:
                for enum_data in builtin_cls_data.enums:
                    name = builtin_cls_data.name + '__' + enum_data.name
                    cls.add(name, PyTypeCategory.ENUM)
                    cls.get(name).inherit = cls.get("Enum")

        
        for enum_data in gdt_all_in_one.global_enums:
            cls.add(enum_data.name, PyTypeCategory.ENUM)
            cls.get(enum_data.name).inherit = cls.get("Enum")

        # 原生类型一定有继承, 继承树的根部是Object
        for cls_data in gdt_all_in_one.classes:
            if cls_data.inherits:
                cls.get(cls_data.name).inherit = cls.get(cls_data.inherits)
            else:
                # 对于Object自身, 应该属于Variant类型, 这里使用继承来表示
                if cls_data.name == "Object":
                    cls.get(cls_data.name).inherit = cls.get("Variant")
                else:
                    raise ValueError(f"Native class '{cls_data.name}' has no inherits")
                
        
        # 内置类的类型是Variant, 这里使用继承来表示
        for builtin_cls_data in gdt_all_in_one.builtin_classes:
            cls.get(builtin_cls_data.name).inherit = cls.get("Variant")
    
    @property
    def is_support_generic(self) -> bool:
        return self in PyType.SUPPORT_GENERIC_TYPES
    
    @property
    def category(self) -> PyTypeCategory:
        if self in PyType.COMPATIBLE_TYPES:
            return PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN
        if self in PyType.SINGLETON_GODOT_NATIVE_TYPES:  # 优先级更高
            return PyTypeCategory.SINGLETON_GODOT_NATIVE
        if self in PyType.ENUM_TYPES:
            return PyTypeCategory.ENUM
        if self in PyType.GODOT_NATIVE_TYPES:
            return PyTypeCategory.GODOT_NATIVE
        if self in PyType.IGNORE_TYPES:
            return PyTypeCategory.IGNORE
        raise ValueError(f"Type {self.name} not found in any category")
    
    @staticmethod
    def parse_name(name: str) -> str:
        result = PyType.try_parse_name(name, raise_error=True)
        if result is None:
            raise ValueError(f"Type not found: {name}")
        return result
    
    @staticmethod
    def try_parse_name(name: str, raise_error: bool = True) -> str|None:
        '''
        尝试转换name, 如果转换失败, 返回None
        '''
        # 内置类型
        if name in PyType.COMPATIBLE_TYPES_MAP:
            return PyType.COMPATIBLE_TYPES_MAP[name]
        
        # 枚举类型
        if name.startswith('enum::'):
            return name.replace('enum::', '').replace('.', "__")
        
        # 也是枚举类型, 包含"."但是不包含"::"的类型
        if '.' in name and '::' not in name:
            return name.replace('.', "__")
        
        # 位域类型
        if name.startswith('bitfield::'):
            return name.replace('bitfield::', '').replace('.', "__")
        
        # typedarray
        if name.startswith('typedarray::'):
            return "Array"
        
        # 正常类型(名字合法的内置类型和原生类型)
        if bool(re.fullmatch(r'[A-Za-z0-9_]+', name)):
            return name
        
        # 引用类型的指针(intptr)
        # "xxx*" / "xxx**"
        if bool(re.fullmatch(r'[A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        # "const xxx*" / "const xxx**"
        if bool(re.fullmatch(r'const [A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        # "xxx,xxx*" / "xxx,xxx**"
        if bool(re.fullmatch(r'[A-Za-z0-9_]+\.[A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        # const xxx.xxx* / const xxx.xxx**
        if bool(re.fullmatch(r'const [A-Za-z0-9_]+\.[A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        
        
        if raise_error:
            raise ValueError(f"Unknown type: {name}")
        return None
    
    
    @staticmethod
    def convert_to_string(pytype: 'PyType', wrap_with_single_quote: bool = True) -> str:
        if wrap_with_single_quote:
            return "'" + pytype.name + "'"
        else:
            return pytype.name
    
    @staticmethod
    def validate(pytype: 'PyType') -> bool:
        results = ValidatorResults()
        results.append(bool(re.fullmatch(r'[A-Za-z0-9_]+', pytype.name)))
        return results.result()


@dataclass
class _ICompositeType:  # MARK: _ICompositeType
    
    def convert_to_string(self) -> str:
        raise NotImplementedError
    
    @staticmethod
    def parse_type(expr: str) -> '_ICompositeType':
        expr = expr.strip()
        
        # 首先尝试解析 Signal 类型
        if expr.startswith('Signal('):
            
            return _SignalType.parse_type(expr)
                
                
        # 如果不是 Signal 类型，则交给 _UnionType 解析
        return _UnionType.parse_type(expr)  # 我们选择将_UnionType放在最外边
    
    def get_used_types(self) -> set[PyType]:
        raise NotImplementedError

    @staticmethod
    def is_type_matched(pytype: 'PyType', composite_type: '_ICompositeType') -> bool:
        return composite_type.is_type_matched(pytype)
    
    def is_type_matched(self, pytype: 'PyType') -> bool:
        raise NotImplementedError
    
    @staticmethod
    def validate(composite_type: '_ICompositeType') -> bool:
        return composite_type.validate()
    
    def validate(self) -> bool:
        raise NotImplementedError

@dataclass
class _UnionType(_ICompositeType):  # MARK: _UnionType
    '''
    class aaa:...
    class bbb[aaa]:...
    class ccc[bbb]:...
    class ddd[aaa]:...
    
    aaa, -bbb, -ccc  ->  aaa|ddd
    aaa, bbb, ccc  ->  aaa|bbb|ccc
    aaa -> aaa
    
    '''
    types: list['_GenericType']
    
    @override
    def validate(self) -> bool:
        return all(type.validate() for type in self.types)

    @override
    def convert_to_string(self) -> str:
        return f"{'|'.join([type.convert_to_string() for type in self.types])}"
    
    @override
    @staticmethod
    def parse_type(expr: str) -> '_UnionType':
        union_exprs = [sub_expr.strip() for sub_expr in expr.split(",")]
        
        if len(union_exprs) == 1:
            return _UnionType([_GenericType.parse_type(expr)])  # 原子类型, 停止递归
        
        union_results = []
        
        #  xxx, -aaa, -bbb, -ccc 模式
        symbol_list: list[str] = []
        for union_expr in union_exprs:
            if union_expr.startswith("-"):
                symbol_list.append('-')
            else:
                symbol_list.append('+')
        
        # 检查是否为 "aaa,-bbb,-ccc" 模式
        if symbol_list[0] == '+' and all(symbol == '-' for symbol in symbol_list[1:]):
            # 排除模式：第一个是基类，其他都是要排除的子类
            base_type = PyType.get(union_exprs[0])
            all_subclasses = PyType.get_subclasses(base_type)
            all_types = [base_type] + all_subclasses
            
            # 要排除的类型
            exclude_types = [PyType.get(expr.lstrip('-')) for expr in union_exprs[1:]]
            
            # 过滤
            filtered_types = [t for t in all_types if t not in exclude_types]
            return _UnionType([_GenericType(t, None) for t in filtered_types])
        else:
            # 普通的联合类型 "aaa,bbb,ccc" 模式
            for union_expr in union_exprs:
                union_results.append(_GenericType.parse_type(union_expr))
        
        return _UnionType(union_results)  # 联合类型, 增加分支并继续递归

    @override
    def get_used_types(self) -> set[PyType]:
        return set().union(*[type.get_used_types() for type in self.types])
    
    @override
    def is_type_matched(self, pytype: 'PyType') -> bool:
        return any(type.is_type_matched(pytype) for type in self.types)

@dataclass
class _GenericType(_ICompositeType):  # MARK: _GenericType
    '''
    typedarray::xxx  --> Array[xxx]
    typedarray::21/9:xxx  --> Array[xxx]
    typedarray::21/9:  --> Array
    typedarray::xxx  --> Array[xxx]
    
    aaa -> aaa
    
    '''
    generic_pytype: PyType
    type_arg: '_UnionType | None'
    
    @override
    def validate(self) -> bool:
        return PyType.validate(self.generic_pytype) and (self.type_arg is None or self.type_arg.validate())

    @override
    def convert_to_string(self) -> str:
        if self.type_arg:
            return f"{self.generic_pytype.name}[{self.type_arg.convert_to_string()}]"
        else:
            return self.generic_pytype.name
    
    @override
    @staticmethod
    def parse_type(expr: str) -> '_GenericType':
        
        # 目前只有typedarray支持泛型
        if expr.startswith('typedarray::'):
            
            # typedarray::21/9:xxx  --> Array[xxx]
            if bool(re.fullmatch(r'typedarray::[0-9]*/[0-9]*:[A-Za-z0-9_]+', expr)):
                inner_type_expr = expr.replace('typedarray::', '').replace(re.search(r'[0-9]*/[0-9]*:', expr).group(), '')
                return _GenericType(PyType.get('Array'), _UnionType.parse_type(inner_type_expr))
            
            # typedarray::21/9:  --> Array
            if bool(re.fullmatch(r'typedarray::[0-9]*/[0-9]*:', expr)):
                return _GenericType(PyType.get('Array'), None)
            
            # typedarray::xxx  --> Array[xxx]
            inner_type_expr = expr.replace('typedarray::', '')
            return _GenericType(PyType.get('Array'), _UnionType.parse_type(inner_type_expr))
        
        elif PyType.get(expr):
            return _GenericType(PyType.get(expr), None)
        
        raise ValueError(f"Unknown type: {expr}")
    
    @override
    def get_used_types(self) -> set[PyType]:
        if self.type_arg:
            return set([self.generic_pytype]).union(self.type_arg.get_used_types())
        else:
            return set([self.generic_pytype])

    @override
    def is_type_matched(self, pytype: 'PyType') -> bool:
        return pytype in PyType.get_subclasses(self.generic_pytype) or pytype == self.generic_pytype
    
@dataclass
class _SignalType(_ICompositeType):  # MARK: _SignalType
    '''
    Signal[Callable[[xxx, xxx, ...], xxx]] -> Signal[typing.Callable[[xxx, xxx, ...], xxx]]
    '''
    return_type: _UnionType
    arguments: list[_UnionType]
    
    @override
    def validate(self) -> bool:
        return self.return_type.validate() and all(arg.validate() for arg in self.arguments)
    
    @override
    def convert_to_string(self) -> str:
        if not self.arguments:
            return f"Signal[{self.return_type.convert_to_string()}]"
        
        args_str = ", ".join([arg.convert_to_string() for arg in self.arguments])
        return f"Signal[typing.Callable[[{args_str}], {self.return_type.convert_to_string()}]]"
    
    @override
    @staticmethod
    def parse_type(expr: str) -> '_SignalType':
        # 检查是否是符合 Signal[Callable[xxx|xxx|xxx|..., xxx]] 格式
        match = re.match(r'Signal\(Callable\(\((.*?)\), ([A-Za-z0-9_]+)\)\)', expr)
        if not match:
            raise ValueError(f"Invalid Signal type format --->{expr}<---")
        
        args_matched = [arg.strip() for arg in match.group(1).split('|')] if '|' in match.group(1) else []
        return_type_matched = match.group(2).strip()

        # 解析参数列表
        arg_types = []
        if args_matched:
            for arg in args_matched:
                arg_types.append(_UnionType.parse_type(arg))
        
        # 解析返回类型
        return_type = _UnionType.parse_type(return_type_matched)
        
        return _SignalType(return_type, arg_types)

    @override
    def get_used_types(self) -> set[PyType]:
        used_types: set[PyType] = set()
        used_types.update(self.return_type.get_used_types())
        for arg in self.arguments:
            used_types.update(arg.get_used_types())
        return used_types
    
    @override
    def is_type_matched(self, pytype: 'PyType') -> bool:
        return pytype is PyType.get('Signal')


@validate_types_on_init
@dataclass
class PyTypeExpr:  # MARK: PyTypeExpr 
    '''
    一个python类型表达式
    '''
    
    composite_types: _ICompositeType
    
        
    ALL_TYPE_EXPRS: ClassVar[dict[str, 'PyTypeExpr']] = {}
    
    @classmethod
    def get(cls, expr: str) -> 'PyTypeExpr':
        if expr in cls.ALL_TYPE_EXPRS:
            return cls.ALL_TYPE_EXPRS[expr]
        else:
            raise ValueError(f"PyTypeExpr --->{expr}<--- is not found")

    @classmethod
    def get_and_add(cls, origin_expr: str) -> 'PyTypeExpr':
        if origin_expr in cls.ALL_TYPE_EXPRS:
            return PyTypeExpr.get(origin_expr)
        
        composite_types = _ICompositeType.parse_type(origin_expr.strip())
        cls.ALL_TYPE_EXPRS[origin_expr] = cls(composite_types)
        return cls.get(origin_expr)
    

        
    @staticmethod
    def convert_to_string(pytype_expr: 'PyTypeExpr', wrap_with_single_quote: bool = True) -> str:
        if wrap_with_single_quote:
            return f"'{pytype_expr.composite_types.convert_to_string()}'"
        else:
            return pytype_expr.composite_types.convert_to_string() 
    
    @staticmethod
    def is_type_matched(pytype: 'PyType', pytype_expr: 'PyTypeExpr|None', strict: bool = True) -> bool:
        if pytype_expr is None:
            return not strict
        return pytype_expr.composite_types.is_type_matched(pytype)
    
    
    @staticmethod
    def get_used_types(pytype_expr: 'PyTypeExpr') -> set[PyType]:
        used_types = set()
        used_types.update(pytype_expr.composite_types.get_used_types())
        return used_types
    

        
    @staticmethod
    def validate(expr: 'PyTypeExpr') -> bool:
        results = ValidatorResults()
        
        results.append(expr.composite_types.validate())
        return results.result()

class PyValueExprCategory(Enum):
    UNKNOWN = 0
    OTHER_TYPE = 1
    NULL = 2
    ENUM_CONST = 3
    INT = 4
    FLOAT = 5
    STR = 6
    BOOL = 7
    STRING_NAME = 8

@validate_types_on_init
@dataclass
class PyValueExpr:  # MARK: PyValueExpr 
    '''
    一个python值(字面量)
    '''
    value_expr: str
    type_expr: PyTypeExpr | None
    
    @cached_property
    def category(self) -> PyValueExprCategory:
        if self.value_expr == 'null':
            return PyValueExprCategory.NULL
        elif self.type_expr is None:
            return PyValueExprCategory.UNKNOWN
        elif PyTypeExpr.is_type_matched(PyType.get('int'), self.type_expr):
            return PyValueExprCategory.INT
        elif PyTypeExpr.is_type_matched(PyType.get('float'), self.type_expr):
            return PyValueExprCategory.FLOAT
        elif PyTypeExpr.is_type_matched(PyType.get('str'), self.type_expr):
            return PyValueExprCategory.STR
        elif PyTypeExpr.is_type_matched(PyType.get('bool'), self.type_expr):
            if self.value_expr.lower() == 'true':
                return PyValueExprCategory.BOOL
            elif self.value_expr.lower() == 'false':
                return PyValueExprCategory.BOOL
            else:
                raise ValueError(f"value expression --->{self.value_expr}<--- is not a valid bool")
        else:
            # enum type
            for enum_type in PyType.ENUM_TYPES:
                if PyTypeExpr.is_type_matched(enum_type, self.type_expr):
                    return PyValueExprCategory.ENUM_CONST

            # other type
            # self.type_expr is not None, so this is other type
            return PyValueExprCategory.OTHER_TYPE
    
    @staticmethod
    def convert_to_string(pyvalue: 'PyValueExpr') -> str:
        
        if pyvalue.category == PyValueExprCategory.NULL:
            return 'null'
        elif pyvalue.category == PyValueExprCategory.ENUM_CONST:
            
            enum_classes: list[PyClass] = []
            
            enum_type: PyType | None = None
            for enum_type in PyType.ENUM_TYPES:
                if PyTypeExpr.is_type_matched(enum_type, pyvalue.type_expr):
                    enum_classes.extend(PyClass.get(enum_type))
                    enum_type = enum_type
            
            enum_value = pyvalue.value_expr
            if len(enum_classes) != 1:
                raise ValueError(f"enum type --->{enum_type}<--- has multiple classes or no classes for value: --->{enum_value}<---  classes: {enum_classes}")
            enum_class = enum_classes[0]
            
            members: list[PyMember] = []
            for member in enum_class.class_attributes:
                # enum 必须有value_expr
                if member.value_expr is None:
                    raise ValueError(f"enum type --->{enum_type}<--- has member --->{member.name}<--- without value_expr")
                if member.value_expr.value_expr == enum_value:
                    members.append(member)
                    
            if len(members) != 1:
                indent = '\n\t'
                raise ValueError(f"enum type --->{enum_type}<--- has multiple members or no members for value: --->{enum_value}<---  {indent}{indent.join(PyClass.convert_to_lines(enum_class))}")
            return members[0].name
        
        elif pyvalue.category == PyValueExprCategory.INT:
            return pyvalue.value_expr
        elif pyvalue.category == PyValueExprCategory.FLOAT:
            return pyvalue.value_expr
        elif pyvalue.category == PyValueExprCategory.STR:
            return pyvalue.value_expr
        elif pyvalue.category == PyValueExprCategory.STRING_NAME:
            return pyvalue.value_expr
        elif pyvalue.category == PyValueExprCategory.BOOL:
            return pyvalue.value_expr
        elif pyvalue.category == PyValueExprCategory.OTHER_TYPE:
            if DEBUG:
                print(f"Warning: value expression: --->{pyvalue.value_expr}<--- type: '{PyTypeExpr.convert_to_string(pyvalue.type_expr, wrap_with_single_quote=False)}' category: {pyvalue.category} has not matched any type")
            return "default(" + repr(pyvalue.value_expr) + ")"
        elif pyvalue.category == PyValueExprCategory.UNKNOWN:
            if DEBUG:
                print(f"Warning: value expression: --->{pyvalue.value_expr}<--- type: '{PyTypeExpr.convert_to_string(pyvalue.type_expr, wrap_with_single_quote=False)}' category: {pyvalue.category} has not matched any type")
            return "default(" + repr(pyvalue.value_expr) + ")"
        else:
            raise ValueError(f"Unknown category: {pyvalue.category}")
    
    @staticmethod
    def validate(value: 'PyValueExpr') -> bool:
        results = ValidatorResults()
        if value.type_expr:
            results.append(PyTypeExpr.validate(value.type_expr))
        return results.result()


@validate_types_on_init
@dataclass
class PyArgument:  # MARK: PyArgument 
    '''
    一个python方法的参数, 可以是带有默认值的键值对参数, 也可以是普通参数
    '''
    name: str
    type_expr: PyTypeExpr
    default_value: PyValueExpr | None = field(default=None)
    
    @staticmethod
    def convert_to_string(argument: 'PyArgument') -> str:
        keyword_underline = ""
        if iskeyword(argument.name):
            keyword_underline = "_"
        if argument.default_value:
            return f"{argument.name}{keyword_underline}: {PyTypeExpr.convert_to_string(argument.type_expr)} = {PyValueExpr.convert_to_string(argument.default_value)}"
        return f"{argument.name}{keyword_underline}: {PyTypeExpr.convert_to_string(argument.type_expr)}"
    
    @staticmethod
    def validate(argument: 'PyArgument') -> bool:
        results = ValidatorResults()
        if argument.type_expr:
            results.append(PyTypeExpr.validate(argument.type_expr))
        else:
            results.append(False)
            
        if argument.default_value:
            results.append(PyValueExpr.validate(argument.default_value))
            results.append(argument.type_expr == argument.default_value.type_expr)
            
        if argument.name:
            results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', argument.name)))
        else:
            results.append(False)
        return results.result()


@validate_types_on_init
@dataclass
class PyMethod:  # MARK: PyMethod 
    '''
    一个python方法, 包含参数, 返回值, 是否是静态方法, 是否是可变长参数
    '''
    name: str
    description_lines: list[str] = field(default_factory=list)
    return_type_expr: PyTypeExpr | None = field(default=None)
    arguments: list[PyArgument] = field(default_factory=list)
    vararg_position: int | None = field(default=None)
    is_static: bool = False
    is_overload: bool = False
    
    OPERATORS_TABLE: dict[str, str] = {
    '<': '__lt__',
    '<=': '__le__',
    '>': '__gt__',
    '>=': '__ge__',
    '==': '__eq__',
    '!=': '__ne__',
    '+': '__add__',
    '-': '__sub__',
    '*': '__mul__',
    '/': '__truediv__',
    '%': '__mod__',
    '**': '__pow__',
    '<<': '__lshift__',
    '>>': '__rshift__',
    '&': '__and__',
    '|': '__or__',
    '^': '__xor__',
    "in": "__contains__",

    'unary-': '__neg__',
    
    '~': '__invert__',
    }

    NOT_SUPPORTED_OPERATORS: dict[str, str] = {
        'unary+': '__pos__',
        'not': '__invert__',
        'and': '__and__',
        'or': '__or__',
        'xor': '__xor__',
    }
    
    def __post_init__(self) -> None:
        new_name = PyMethod.try_parse_name(self.name)
        if new_name == None:
            raise ValueError(f"Operator is not supported: {self.name}")
        self.name = new_name
    
    @staticmethod
    def try_parse_name(name: str) -> str | None:
        
        # 运算符
        if name in PyMethod.OPERATORS_TABLE:
            return PyMethod.OPERATORS_TABLE[name]
        
        # 不支持的运算符
        if name in PyMethod.NOT_SUPPORTED_OPERATORS:
            return None
        
        # 正常方法名
        if bool(re.fullmatch(r'[A-Za-z0-9_]+', name)):
            return name
        
        # 未知运算符或非法方法名
        raise ValueError(f"Invalid method name or operator: {name}")

    @staticmethod
    def convert_to_lines(method: 'PyMethod') -> list[str]:
        lines: list[str] = []
        
        # @staticmethod
        if method.is_static:
            lines.append('@staticmethod')
        
        # @overload
        if method.is_overload:
            lines.append('@overload')
        
        # def xxx(xxx: xxx, xxx: xxx, *args, xxx: xxx = xxx) -> xxx:
        args_expr: list[str] = []
        if not method.is_static:
            args_expr.append('self')
            
        for i,arg in enumerate(method.arguments):
            if i == method.vararg_position:
                args_expr.append('*args')
            else:
                args_expr.append(PyArgument.convert_to_string(arg))

        return_type_expr = PyTypeExpr.convert_to_string(method.return_type_expr) if method.return_type_expr else "None"
        
        keyword_underline = ""
        if iskeyword(method.name):
            keyword_underline = "_"
        lines.append(f'def {method.name}{keyword_underline}({", ".join(args_expr)}) -> {return_type_expr}:')
        
        # """description
        #
        # description
        # """
        if method.description_lines:
            lines.extend([f'    {line}' for line in method.description_lines])
            
            # ...
            lines.append('    ...')
        else:
            lines[-1] += ' ...'
        
        return lines
    
    @staticmethod
    def validate(method: 'PyMethod') -> bool:
        results = ValidatorResults()
        if method.return_type_expr:
            results.append(PyTypeExpr.validate(method.return_type_expr))
        else:
            results.append(False)
            
        for argument in method.arguments:
            results.append(PyArgument.validate(argument))
            
        return results.result()


@validate_types_on_init
@dataclass
class SpecifiedPyMember:
    specified_string: str
    inline_comment: str|None = field(default=None)
    
    @staticmethod
    def convert_to_string(specified_py_member: 'SpecifiedPyMember') -> str:
        s = specified_py_member.specified_string
        if specified_py_member.inline_comment:
            s += f"  # {specified_py_member.inline_comment}"
        return s
    
    @staticmethod
    def validate(specified_py_member: 'SpecifiedPyMember') -> bool:
        return True
    
@validate_types_on_init
@dataclass
class PyMember:  # MARK: PyMember 
    '''
    一个python属性(赋值语句), 包含名称, 类型, 内联注释
    '''
    name: str
    type_expr: PyTypeExpr
    value_expr: PyValueExpr | None = field(default=None)
    inline_comment: str|None = field(default=None)
    
    @staticmethod
    def convert_to_string(member: 'PyMember', type_annotation_mode: Literal['explicit', 'comment', 'none'] = 'explicit') -> str:
        keyword_underline = ""
        if iskeyword(member.name):
            keyword_underline = "_"
        s = f'{member.name}{keyword_underline}{": "+PyTypeExpr.convert_to_string(member.type_expr) if type_annotation_mode == "explicit" else ""}'
        if member.value_expr:
            s += f' = {PyValueExpr.convert_to_string(member.value_expr)}'

        if type_annotation_mode == "comment" or member.inline_comment:
            comment_parts: list[str] = []
            
            # 只有comment模式才会添加类型注解到注释中
            if type_annotation_mode == "comment":
                comment_parts.append(f"type: {PyTypeExpr.convert_to_string(member.type_expr)}")
            
            # 无论何种模式下, 若存在inline_comment, 那么都显示内联注释
            if member.inline_comment:
                comment_parts.append(f"comment: {member.inline_comment}")
            
            if comment_parts:
                s += f"  # {' '.join(comment_parts)}"
                
        return s

    @staticmethod
    def validate(member: 'PyMember') -> bool:
        results = ValidatorResults()
        
        if member.type_expr:
            results.append(PyTypeExpr.validate(member.type_expr))
        else:
            results.append(False)
        
        if member.value_expr:
            results.append(PyValueExpr.validate(member.value_expr))
            results.append(member.type_expr == member.value_expr.type_expr)
        
        if member.name:
            results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', member.name)))
        else:
            results.append(False)
            
        return results.result()

class PyClassCategory(Enum):
    PY_CLASS = "PY_CLASS"
    PY_SINGLETON = "PY_SINGLETON"

@validate_types_on_init
@dataclass
class PyClass:  # MARK: PyClass 
    '''
    一个python类, 包含类型, 描述, 成员, 类属性, 方法
    '''
    type: PyType
    description_lines: list[str] = field(default_factory=list)
    
    members: list[PyMember] = field(default_factory=list)
    class_attributes: list[PyMember] = field(default_factory=list)
    methods: list[PyMethod] = field(default_factory=list)
    
    CLASS_NAME_ALIAS: ClassVar[dict[str, str]] = {"str":"String", "int": "Int", "float": "Float", "bool": "Bool"}
    CLASS_IGNORED: ClassVar[set[str]] = {"None"}
    
    ALL_CLASSES: ClassVar[dict['PyType', list['PyClass']]] = {}
    
    def __post_init__(self):
        if self.type not in PyClass.ALL_CLASSES:
            PyClass.ALL_CLASSES[self.type] = []
        PyClass.ALL_CLASSES[self.type].append(self)
    
    @staticmethod
    def get(pytype: 'PyType') -> list['PyClass']:
        # 由于一个类型可能对应多个PyClass实例, 因此这里并不强制约束PyClass和PyType的一对一关系, 而是返回所有可能的PyClass实例, 并实现两者在附属关系上的松耦合
        
        return PyClass.ALL_CLASSES[pytype]
    
    @staticmethod
    def _is_empty_class(pyclass: 'PyClass') -> bool:
        return not pyclass.members and not pyclass.class_attributes and not pyclass.methods

    @staticmethod
    def get_category(pyclass: 'PyClass') -> PyTypeCategory:
        return pyclass.type.category
    
    
    @staticmethod
    def get_used_types(pyclass: 'PyClass') -> set[PyType]:
        used_types: set[PyType] = set()
        used_types.add(pyclass.type)
        if pyclass.type.inherit:
            used_types.add(pyclass.type.inherit)
        for member in pyclass.members:
            if member.type_expr:
                used_types.update(PyTypeExpr.get_used_types(member.type_expr))
        for class_attribute in pyclass.class_attributes:
            if class_attribute.type_expr:
                used_types.update(PyTypeExpr.get_used_types(class_attribute.type_expr))
        for method in pyclass.methods:
            if method.return_type_expr:
                used_types.update(PyTypeExpr.get_used_types(method.return_type_expr))
            for argument in method.arguments:
                if argument.type_expr:
                    used_types.update(PyTypeExpr.get_used_types(argument.type_expr))
        return used_types
    
    @staticmethod
    def convert_to_lines(pyclass: 'PyClass') -> list[str]:
        lines: list[str] = []
        
        # 忽略某些类
        class_name = PyType.convert_to_string(pyclass.type, wrap_with_single_quote=False)
        if class_name in PyClass.CLASS_IGNORED:
            if DEBUG:
                print(f"Warning: Class '{class_name}' is ignored")
            return []
        
        # 防止和python内置类型重名
        if class_name in PyClass.CLASS_NAME_ALIAS:
            class_name = PyClass.CLASS_NAME_ALIAS[class_name]
            
        # class xxx(xxx):
        
        GENERIC_TYPES = {
                "Signal": "[T: Callable]",
                "Callable": "[T, R]",
                "Array": "[T]",
            }
        generic_annotation = GENERIC_TYPES.get(class_name, "")
        
        inherit_annotation = "" if not pyclass.type.inherit else f'({PyType.convert_to_string(pyclass.type.inherit, wrap_with_single_quote=False)})'
        
        class_definition_line = f'class {class_name}{generic_annotation}{inherit_annotation}:'
        
        lines.append(class_definition_line)
        
        
        # class xxx(xxx): ...
        if PyClass._is_empty_class(pyclass) and not pyclass.description_lines:
            lines[-1] += ' ...'
            return lines
        
        
        # class xxx(xxx):
        #     """description
        #
        #     description
        #     """
        #     ...
        #
        if PyClass._is_empty_class(pyclass) and pyclass.description_lines:
            lines.extend([f'    {line}' for line in pyclass.description_lines])
            lines.append('    ...')
        
        
        # class xxx(xxx):
        #     """description
        #
        #     description
        #     """
        #
        #     xxx: xxx = xxx
        #     def xxx(xxx: xxx, xxx: xxx, *args, xxx: xxx = xxx) -> xxx: ...
        #
        if pyclass.description_lines:
            lines.extend([f'    {line}' for line in pyclass.description_lines])
        
        # class attributes
        if pyclass.type.category != PyTypeCategory.ENUM:
            for member in pyclass.class_attributes:
                type_annotation_mode = 'comment'
                lines.append("    " + PyMember.convert_to_string(member, type_annotation_mode = type_annotation_mode))
        else:
            enum_const_type_list: list[PyTypeExpr] = []
            for member in pyclass.class_attributes:
                if not member.value_expr:
                    raise ValueError(f"Enum member '{member.name}' has no value_expr")
                if member.value_expr.category != PyValueExprCategory.INT:
                    raise ValueError(f"Enum member '{member.name}'='{member.value_expr}' is not INT")
                enum_const_type_list.append(member.type_expr)
            
            for enum_const_type in enum_const_type_list:
                lines.append("    " + PyTypeExpr.convert_to_string(enum_const_type, wrap_with_single_quote=False))
            
        # instance members
        for member in pyclass.members:
            lines.append("    " + PyMember.convert_to_string(member))
        
        # class methods
        for method in pyclass.methods:
            lines.extend([f'    {line}' for line in PyMethod.convert_to_lines(method)])

        return lines
    
    @staticmethod
    def validate(pyclass: 'PyClass') -> bool:
        results = ValidatorResults()
        results.append(PyType.validate(pyclass.type))
        for member in pyclass.members:
            results.append(PyMember.validate(member))
        for class_attribute in pyclass.class_attributes:
            results.append(PyMember.validate(class_attribute))
        for method in pyclass.methods:
            results.append(PyMethod.validate(method))
        return results.result()

    @staticmethod
    def build_dependency_graph(pyclasses: list['PyClass']) -> dict[str, list[str]]:
        """
        构建类依赖图，基于类型使用关系
        """
        def get_name(pyclass: 'PyClass') -> str:
            return pyclass.type.name
            
        def get_dependencies(pyclass: 'PyClass') -> list[str]:
            used_types = PyClass.get_used_types(pyclass)
            return [used_type.name for used_type in used_types]
            
        return build_dependency_graph(pyclasses, get_name, get_dependencies)



@validate_types_on_init
@dataclass
class PyFile:  # MARK: PyFile
    name: str
    
    imports: list[str] = field(default_factory=list)
    description_lines: list[str] = field(default_factory=list)
    
    global_variables: list[PyMember|SpecifiedPyMember] = field(default_factory=list)
    global_functions: list[PyMethod] = field(default_factory=list)
    classes: list[PyClass] = field(default_factory=list)
    
    @staticmethod
    def convert_to_lines(pyfile: 'PyFile') -> list[str]:
        lines: list[str] = []
        
        # from xxx import xxx
        lines.extend(pyfile.imports)
        lines.append('')
        lines.append('')
        
        # """description
        #
        # description
        # """
        if pyfile.description_lines:
            lines.extend(pyfile.description_lines)
            lines.append('')
            lines.append('')
        
        # global variables
        for variable in pyfile.global_variables:
            lines.append(PyMember.convert_to_string(variable) if isinstance(variable, PyMember) else SpecifiedPyMember.convert_to_string(variable))
            lines.append('')
        
        # global functions
        for function in pyfile.global_functions:
            lines.extend(PyMethod.convert_to_lines(function))
            lines.append('')
        
        # classes
        # 根据继承的先后关系, 先添加父类, 再添加子类
        
        # 提取所有类的类型
        class_map = {pyclass.type.name: pyclass for pyclass in pyfile.classes}
        
        # 同时考虑继承关系和类型使用关系
        
        # 构建类型使用依赖图
        usage_graph = PyClass.build_dependency_graph(pyfile.classes)
        
        
        # 对依赖图进行拓扑排序
        ordered_class_names = topological_sort(usage_graph)
        ordered_class_names.reverse()
        
        # 按照排序后的顺序添加类
        for class_name in ordered_class_names:
            if class_name in class_map:
                pyclass = class_map[class_name]
                lines.extend(PyClass.convert_to_lines(pyclass))
                lines.append('')
                lines.append('')
        
        # 添加没有在排序结果中的剩余类（可能是没有依赖关系的类）
        remaining_classes = [pyclass for pyclass in pyfile.classes if pyclass.type.name not in ordered_class_names]
        for pyclass in remaining_classes:
            lines.extend(PyClass.convert_to_lines(pyclass))
            lines.append('')
        
        return lines

    @staticmethod
    def validate(pyfile: 'PyFile') -> bool:
        results = ValidatorResults()
        for variable in pyfile.global_variables:
            results.append(PyMember.validate(variable) if isinstance(variable, PyMember) else SpecifiedPyMember.validate(variable))
        for function in pyfile.global_functions:
            results.append(PyMethod.validate(function))
        for pyclass in pyfile.classes:
            results.append(PyClass.validate(pyclass))
        return results.result()


