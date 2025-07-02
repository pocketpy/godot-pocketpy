from dataclasses import dataclass, field, fields
from enum import Enum
import re
from typing import ClassVar, Literal

from .tools import validate_types_on_init, ValidatorResults, DEBUG, build_dependency_graph, topological_sort
from .schema_gdt import GodotInOne
from keyword import iskeyword



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
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, PyType):
            return False
        return self.name == other.name
    
    @classmethod
    def get(cls, name: str, raise_error: bool = True) -> 'PyType | None':
        '''
        根据名字获取PyType, 设计时只允许用来获取原子类型
        '''
        name = PyType.try_parse_name(name)
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
        name = PyType.try_parse_name(name)
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
    def try_parse_name(name: str, raise_error: bool = True) -> str|None:
        '''
        尝试转换name
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
        
        # 无法转换的类型
        if name.startswith('Signal'):
            raise ValueError(f"Signal type is not supported, please use PyTypeExpr.get_and_add_specified('{name}')")
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




@validate_types_on_init
@dataclass
class PyTypeExpr:  # MARK: PyTypeExpr 
    '''
    一个python类型表达式
    '''
    
    composite_types: list[tuple|None] = field(default_factory=lambda: [None])  # tuple[PyType, tuple[PyType, tuple[PyType, ...] | None] | None] | None
    specified_string: str | None = field(default=None)  # 如果指定了字符串, 那么convert_to_string将直接返回这个字符串, 同时validate将返回True
    
    ALL_TYPE_EXPRS: ClassVar[dict[str, 'PyTypeExpr']] = {}
    
    @classmethod
    def get(cls, expr: str) -> 'PyTypeExpr':
        if expr in cls.ALL_TYPE_EXPRS:
            return cls.ALL_TYPE_EXPRS[expr]
        else:
            raise ValueError(f"PyTypeExpr --->{expr}<--- is not found")
    
    @staticmethod
    def try_parse_generic_expr(expr: str) -> tuple['PyType', str] | None:
        
        # 目前只有typedarray支持泛型
        if expr.startswith('typedarray::'):
            
            # typedarray::21/9:xxx  --> Array[xxx]
            if bool(re.fullmatch(r'typedarray::[0-9]*/[0-9]*:[A-Za-z0-9_]+', expr)):
                return (PyType.get('Array'), expr.replace('typedarray::', '').replace(re.search(r'[0-9]*/[0-9]*:', expr).group(), ''))
            
            # typedarray::21/9:  --> Array
            if bool(re.fullmatch(r'typedarray::[0-9]*/[0-9]*:', expr)):
                return None
            
            # typedarray::xxx  --> Array[xxx]
            return (PyType.get('Array'), expr.replace('typedarray::', ''))
        
            
        
        return None
    
    @staticmethod
    def try_parse_union_expr(expr: str) -> list[str]:
        return [sub_expr.strip() for sub_expr in expr.split(",")]
    
    @staticmethod
    def _recursive_parse_type(origin_expr: str) -> list[tuple['PyType', str|None]]:
        # TODO 在运行时会遇到一个报错: ValueError: Unknown type: Array[StringName], 这是因为Array[xxx]来自于原始字符串typedarray::xxx, 虽然能够处理从typedarray::xxx -> Array[xxx]的映射, 但是由于存在结构性问题, 导致在处理specified_string(也即Signal这一特例的类型注解)时会多调用一次try_parse_generic_expr, 因此导致无法使用.
        # TODO 解决方案是将Signal这一特例也加入到格式化解析的逻辑中, 从而彻底去除任何特例(也即从此不需要字段PyType.specified_string). 这可能需要重新规划PyType.composite_type的结构, 并重构以上两个字段相关的所有逻辑.
        
        
        generic_result = PyTypeExpr.try_parse_generic_expr(origin_expr)
        if generic_result:
            return [(generic_result[0], PyTypeExpr._recursive_parse_type(generic_result[1]))]  # 泛型类型, 继续递归
        
        union_exprs = PyTypeExpr.try_parse_union_expr(origin_expr)
        
        if len(union_exprs) == 1:
            return [(PyType.get(origin_expr), None)]  # 原子类型, 停止递归
        
        union_results = []
        
        #  xxx, -aaa, -bbb, -ccc 模式
        symbol_list = []
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
            return [(t, None) for t in filtered_types]
        else:
            # 普通的联合类型 "aaa,bbb,ccc" 模式
            for union_expr in union_exprs:
                result = PyTypeExpr._recursive_parse_type(union_expr)
                union_results.extend(result)
        
        return union_results  # 联合类型, 增加分支并继续递归
        
    
    @classmethod
    def get_and_add(cls, origin_expr: str) -> 'PyTypeExpr':
        if origin_expr in cls.ALL_TYPE_EXPRS:
            return PyTypeExpr.get(origin_expr)
        
        composite_types = PyTypeExpr._recursive_parse_type(origin_expr.strip())
        cls.ALL_TYPE_EXPRS[origin_expr] = cls(composite_types)
        return cls.get(origin_expr)
    
    @classmethod
    def get_and_add_specified(cls, specified_string: str) -> 'PyTypeExpr':
        if specified_string in cls.ALL_TYPE_EXPRS:
            return PyTypeExpr.get(specified_string)
        
        cls.ALL_TYPE_EXPRS[specified_string] = cls(specified_string=specified_string)
        return cls.get(specified_string)
        
    @staticmethod
    def _recursive_convert_to_string(composite_types: list[tuple['PyType', list[tuple['PyType', list[tuple['PyType', list[tuple['PyType', ...] | None] | None] | None] | None] | None] | None]]) -> str:
        
        
        s = " | ".join([PyType.convert_to_string(composite_type[0], wrap_with_single_quote=False) if composite_type[1] is None else f"{PyType.convert_to_string(composite_type[0], wrap_with_single_quote=False)}[{PyTypeExpr._recursive_convert_to_string(composite_type[1])}]" for composite_type in composite_types])
        
        return s
        
        
    @staticmethod
    def convert_to_string(pytype_expr: 'PyTypeExpr', wrap_with_single_quote: bool = True) -> str:
        if pytype_expr.specified_string:
            if wrap_with_single_quote:
                return "'" + pytype_expr.specified_string + "'"
            else:
                return pytype_expr.specified_string
        
        return PyTypeExpr._recursive_convert_to_string(pytype_expr.composite_types)
    
    @staticmethod
    def is_type_matched(pytype: 'PyType', pytype_expr: 'PyTypeExpr') -> bool:
        if pytype_expr.specified_string:
            raise ValueError(f"specified string --->{pytype_expr.specified_string}<--- is not supported")
        
        matched = []
        for composite_type in pytype_expr.composite_types:
            if pytype == composite_type[0] or pytype in PyType.get_subclasses(composite_type[0]):
                matched.append(True)
                break
            else:
                matched.append(False)
        
        return any(matched)
    
    @staticmethod
    def _recursive_get_used_types(composite_types: list[tuple['PyType', list[tuple['PyType', list[tuple['PyType', list[tuple['PyType', ...] | None] | None] | None] | None] | None] | None]]) -> set[PyType]:
        used_types = set()
        for composite_type in composite_types:
            if composite_type[1] is None:
                used_types.add(composite_type[0])
            else:
                used_types.add(composite_type[0])
                used_types.update(PyTypeExpr._recursive_get_used_types(composite_type[1]))
        return used_types
    
    @staticmethod
    def get_used_types(pytype_expr: 'PyTypeExpr') -> set[PyType]:
        used_types = set()
        print(pytype_expr)
        
        # 处理Signal[Callable[[xxx, xxx, ...], xxx]]类型
        if pytype_expr.specified_string is not None:
            signal_pattern = r'Signal\[Callable\[\[(.*?)\], ([A-Za-z0-9_]+)\]\]'
            signal_match = re.match(signal_pattern, pytype_expr.specified_string)
            if signal_match:
                args_types = signal_match.group(1).split(',') if signal_match.group(1) != '' else []
                args_types = [arg_type.strip() for arg_type in args_types]
                return_type = signal_match.group(2).strip() if signal_match.group(2) != 'None' else None
                
                for arg_type in args_types:
                    used_types.update(PyTypeExpr.get_used_types(PyTypeExpr.get_and_add(arg_type)))

                if return_type:
                    used_types.update(PyTypeExpr.get_used_types(PyTypeExpr.get_and_add(return_type)))
                
                used_types.update(set([PyType.get('Signal'), PyType.get('Callable')]))
                return used_types
            else:
                raise ValueError(f"specified string --->{pytype_expr.specified_string}<--- is not supported")
        
        # 处理一般类型
        used_types.update(PyTypeExpr._recursive_get_used_types(pytype_expr.composite_types))
        return used_types
    
    @staticmethod
    def _recursive_validate(composite_type: tuple['PyType', tuple['PyType', tuple['PyType', ...] | None] | None]) -> bool:
        if composite_type[1] is None:
            return PyType.validate(composite_type[0])
        return PyType.validate(composite_type[0]) and PyTypeExpr._recursive_validate(composite_type[1])
    
    @staticmethod
    def validate(expr: 'PyTypeExpr') -> bool:
        results = ValidatorResults()
        
        if expr.specified_string:
            return True
        
        results.append(PyTypeExpr._recursive_validate(expr.composite_type))
        return results.result()


@validate_types_on_init
@dataclass
class PyValueExpr:  # MARK: PyValueExpr 
    '''
    一个python值(字面量)
    '''
    value_expr: str
    type_expr: PyTypeExpr | None
    
    @staticmethod
    def convert_to_string(value: 'PyValueExpr') -> str:
        
        default_str = "default(" + repr(value.value_expr) + ")"
        
        
        if not value.type_expr:
            raise ValueError(f"value expression --->{value.value_expr}<--- has no type")
        
        if value.value_expr == 'null':
            return default_str
        
        if PyTypeExpr.is_type_matched(PyType.get('int'), value.type_expr):
            return value.value_expr
        elif PyTypeExpr.is_type_matched(PyType.get('float'), value.type_expr):
            return value.value_expr
        elif PyTypeExpr.is_type_matched(PyType.get('str'), value.type_expr):
            return value.value_expr
        elif PyTypeExpr.is_type_matched(PyType.get('StringName'), value.type_expr):
            return default_str
        elif PyTypeExpr.is_type_matched(PyType.get('bool'), value.type_expr):
            if value.value_expr.lower() == 'true':
                return 'True'
            elif value.value_expr.lower() == 'false':
                return 'False'
            else:
                raise ValueError(f"value expression --->{value.value_expr}<--- is not a valid bool")
        else:
            
            for enum_class in PyType.ENUM_TYPES:
                if PyTypeExpr.is_type_matched(enum_class, value.type_expr):
                    return value.value_expr
            else:
                if DEBUG:
                    print(f"Warning: value expression: --->{value.value_expr}<--- type: '{PyTypeExpr.convert_to_string(value.type_expr, wrap_with_single_quote=False)}' has not matched any type")
                return default_str
    
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
    return_type_expr: PyTypeExpr | None = field(default=None)
    is_static: bool = False
    is_overload: bool = False
    
    OPERATORS_TABLE = {
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

    NOT_SUPPORTED_OPERATORS = {
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
        lines = []
        
        # @staticmethod
        if method.is_static:
            lines.append('@staticmethod')
        
        # @overload
        if method.is_overload:
            lines.append('@overload')
        
        # def xxx(xxx: xxx, xxx: xxx, *args, xxx: xxx = xxx) -> xxx:
        args_expr = []
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
class PyMember:  # MARK: PyMember 
    '''
    一个python属性(赋值语句), 包含名称, 类型, 内联注释
    '''
    specified_string: str | None = field(default=None)  # 如果指定了字符串, 那么convert_to_string将直接返回这个字符串, 同时validate将返回True
    name: str | None = field(default=None)
    type_expr: PyTypeExpr | None = field(default=None)
    value_expr: PyValueExpr | None = field(default=None)
    inline_comment: str|None = field(default=None)
    
    @staticmethod
    def convert_to_string(member: 'PyMember', type_annotation_mode: Literal['explicit', 'comment', 'none'] = 'explicit') -> str:
        if member.specified_string is not None:
            return member.specified_string
        keyword_underline = ""
        if iskeyword(member.name):
            keyword_underline = "_"
        s = f'{member.name}{keyword_underline}{": "+PyTypeExpr.convert_to_string(member.type_expr) if type_annotation_mode == "explicit" else ""}'
        if member.value_expr:
            s += f' = {PyValueExpr.convert_to_string(member.value_expr)}'

        
        if member.inline_comment or type_annotation_mode == "comment":
            
            type_annotation = " type: "+PyTypeExpr.convert_to_string(member.type_expr) if type_annotation_mode == "comment" else ""
            
            additional_comment = f' comment: {member.inline_comment}' if member.inline_comment else ""
            
            s += f"  #{type_annotation}{additional_comment}"
        return s

    @staticmethod
    def validate(member: 'PyMember') -> bool:
        results = ValidatorResults()
        if member.specified_string is not None:
            return True
        
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
    
    @staticmethod
    def _is_empty_class(pyclass: 'PyClass') -> bool:
        return not pyclass.members and not pyclass.class_attributes and not pyclass.methods

    @staticmethod
    def get_category(pyclass: 'PyClass') -> PyTypeCategory:
        return pyclass.type.category
    
    
    @staticmethod
    def get_used_types(pyclass: 'PyClass') -> set[PyType]:
        used_types = set()
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
        lines = []
        
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
        if pyclass.type.inherit:
            lines.append(f'class {class_name}({PyType.convert_to_string(pyclass.type.inherit, wrap_with_single_quote=False)}):')
        else:
            lines.append(f'class {class_name}:')
        
        
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
        lines.append('')
        
        # class attributes
        for member in pyclass.class_attributes:
            type_annotation_mode = 'comment' if pyclass.type.category == PyTypeCategory.ENUM else 'none'
            lines.append("    " + PyMember.convert_to_string(member, type_annotation_mode = type_annotation_mode))
        lines.append('')
        
        # instance members
        for member in pyclass.members:
            lines.append("    " + PyMember.convert_to_string(member))
        lines.append('')
        
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
        def get_name(pyclass):
            return pyclass.type.name
            
        def get_dependencies(pyclass):
            used_types = PyClass.get_used_types(pyclass)
            return [used_type.name for used_type in used_types]
            
        return build_dependency_graph(pyclasses, get_name, get_dependencies)



@validate_types_on_init
@dataclass
class PyFile:  # MARK: PyFile
    name: str
    
    imports: list[str] = field(default_factory=list)
    description_lines: list[str] = field(default_factory=list)
    
    global_variables: list[PyMember] = field(default_factory=list)
    global_functions: list[PyMethod] = field(default_factory=list)
    classes: list[PyClass] = field(default_factory=list)
    
    @staticmethod
    def convert_to_lines(pyfile: 'PyFile') -> list[str]:
        lines = []
        
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
            lines.append(PyMember.convert_to_string(variable))
        lines.append('')
        
        # global functions
        for function in pyfile.global_functions:
            lines.extend(PyMethod.convert_to_lines(function))
        lines.append('')
        
        # classes
        # 根据继承的先后关系, 先添加父类, 再添加子类
        
        # 提取所有类的类型
        pytypes = [pyclass.type for pyclass in pyfile.classes]
        class_map = {pyclass.type.name: pyclass for pyclass in pyfile.classes}
        
        # 同时考虑继承关系和类型使用关系
        
        # 构建类型使用依赖图
        usage_graph = PyClass.build_dependency_graph(pyfile.classes)
        
        
        # 对依赖图进行拓扑排序
        ordered_class_names = topological_sort(usage_graph)
        
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
            results.append(PyMember.validate(variable))
        for function in pyfile.global_functions:
            results.append(PyMethod.validate(function))
        for pyclass in pyfile.classes:
            results.append(PyClass.validate(pyclass))
        return results.result()


