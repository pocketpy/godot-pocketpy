from dataclasses import dataclass, field, fields
from enum import Enum
import re
from typing import ClassVar

from .tools import validate_types_on_init, ValidatorResults
from .schema_gdt import GodotInOne



class PyTypeCategory(Enum):
    CAN_TRANSFER_TO_PY_BUILTIN = "CAN_TRANSFER_TO_PY_BUILTIN"
    GODOT_NATIVE = "GODOT_NATIVE"
    ENUM = "ENUM"
    SINGLETON_GODOT_NATIVE = "SINGLETON_GODOT_NATIVE"


@validate_types_on_init
@dataclass
class PyType:
    '''
    一个python类型
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
    BUILTIN_TYPES: ClassVar[dict[str, str]] = {"Nil":'None', "int":'int', "float":'float', "bool":'bool', "String":'str'}
    
    ALL_TYPES: ClassVar[dict[str, 'PyType']] = {}
    
    
    # Type categorization sets
    CAN_TRANSFER_TO_PY_BUILTIN_TYPES: ClassVar[set['PyType']] = set()
    GODOT_NATIVE_TYPES: ClassVar[set['PyType']] = set()
    ENUM_TYPES: ClassVar[set['PyType']] = set()
    SINGLETON_GODOT_NATIVE_TYPES: ClassVar[set['PyType']] = set()
    
    inherit: 'PyType | None' = field(default=None)
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, PyType):
            return False
        return self.name == other.name
    
    @classmethod
    def get(cls, name: str) -> 'PyType':
        '''
        根据名字获取PyType
        '''
        name = name.replace('.', "__")
        name = name.replace('enum::', "")
        name = name.replace('bitfield::', "")
        pytype = PyType.ALL_TYPES[name]
        return pytype
    
    @classmethod
    def add(cls, name: str, category: PyTypeCategory) -> None:
        '''
        添加一个PyType, 此处为系统收录类型的唯一门户, 注意保证name的干净
        '''

        name = name.replace('.', "__")
        name = name.replace('enum::', "")
        name = name.replace('bitfield::', "")

        new_pytype = PyType(name=name)
        if not PyType.validate(new_pytype):
            raise ValueError(f"Invalid type: {name}")
        
        cls.ALL_TYPES[name] = new_pytype
        cls.add_type_to_category(new_pytype, category)
    
    @classmethod
    def add_type_to_category(cls, pytype: 'PyType', category: PyTypeCategory) -> None:
        """
        将一个PyType添加到指定的类别集合中
        """
        if category == PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN:
            cls.CAN_TRANSFER_TO_PY_BUILTIN_TYPES.add(pytype)
        elif category == PyTypeCategory.GODOT_NATIVE:
            cls.GODOT_NATIVE_TYPES.add(pytype)
        elif category == PyTypeCategory.ENUM:
            cls.ENUM_TYPES.add(pytype)
        elif category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
            cls.SINGLETON_GODOT_NATIVE_TYPES.add(pytype)
        else:
            raise ValueError(f"Invalid category: {category}")
        
    
    @classmethod
    def build_type_map(cls, gdt_all_in_one: GodotInOne) -> None:
        '''
        从gdt_all_in_one构建PyType.ALL_TYPES
        '''
        for singleton_data in gdt_all_in_one.singletons:
            cls.add(singleton_data.name, PyTypeCategory.SINGLETON_GODOT_NATIVE)
        
        for builtin_class in gdt_all_in_one.builtin_classes:
            cls.add(builtin_class.name, PyTypeCategory.GODOT_NATIVE)
        
        for cls_data in gdt_all_in_one.classes:
            
            cls.add(cls_data.name, PyTypeCategory.GODOT_NATIVE)
            
            if cls_data.enums:
                for enum_data in cls_data.enums:
                    name = cls_data.name + '__' + enum_data.name
                    cls.add(name, PyTypeCategory.ENUM)
                    
            cls.add(cls_data.name, PyTypeCategory.GODOT_NATIVE)
        
        for enum_data in gdt_all_in_one.global_enums:
            cls.add(enum_data.name, PyTypeCategory.ENUM)

        # inherits
        for cls_data in gdt_all_in_one.classes:
            if cls_data.inherits:
                cls.get(cls_data.name).inherit = cls.get(cls_data.inherits)
    
    @property
    def category(self) -> PyTypeCategory:
        if self in PyType.CAN_TRANSFER_TO_PY_BUILTIN_TYPES:
            return PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN
        if self in PyType.SINGLETON_GODOT_NATIVE_TYPES:  # 优先级更高
            return PyTypeCategory.SINGLETON_GODOT_NATIVE
        if self in PyType.ENUM_TYPES:
            return PyTypeCategory.ENUM
        if self in PyType.GODOT_NATIVE_TYPES:
            return PyTypeCategory.GODOT_NATIVE
        
        raise ValueError(f"Type {self.name} not found in any category")
    
    @staticmethod
    def try_parse_name(name: str) -> str:
        '''
        尝试转换name
        '''
        # 内置类型
        if name in PyType.BUILTIN_TYPES:
            return PyType.BUILTIN_TYPES[name]
        
        # 枚举类型
        if name.startswith('enum::'):
            return name.replace('enum::', '').replace('.', "__")
        
        # 正常类型(名字合法的内置类型和原生类型)
        if bool(re.fullmatch(r'[A-Za-z0-9]+', name)):
            return name
        
        # 无法转换的类型
        raise ValueError(f"Invalid type: {name}")
    
    @staticmethod
    def convert_to_string(type: 'PyType') -> str:
        if type.category == PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN:
            return type.name
        elif type.category == PyTypeCategory.GODOT_NATIVE:
            return type.name
        elif type.category == PyTypeCategory.ENUM:
            return type.name
        elif type.category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
            return type.name
        else:
            raise ValueError(f"Invalid type: {type.name}")
        
    @staticmethod
    def validate(type: 'PyType') -> bool:
        results = ValidatorResults()
        results.append(bool(re.fullmatch(r'[A-Za-z0-9_]+', type.name)))
        return results.result()

@validate_types_on_init
@dataclass
class PyTypeExpr:
    '''
    一个python类型表达式
    '''
    type: PyType | None
    expr: str

    @staticmethod
    def convert_to_string(expr: 'PyTypeExpr') -> str:
        if expr.type:
            return PyType.convert_to_string(expr.type)
        return expr.expr
    
    @staticmethod
    def validate(expr: 'PyTypeExpr') -> bool:
        results = ValidatorResults()
        if expr.type:
            results.append(PyType.validate(expr.type))
        return results.result()


@validate_types_on_init
@dataclass
class PyValueExpr:
    '''
    一个python值(字面量)
    '''
    expr: str
    type_expr: PyTypeExpr | None
    
    @staticmethod
    def convert_to_string(value: 'PyValueExpr') -> str:
        return value.expr
    
    @staticmethod
    def validate(value: 'PyValueExpr') -> bool:
        results = ValidatorResults()
        if value.type_expr:
            results.append(PyTypeExpr.validate(value.type_expr))
        return results.result()


@validate_types_on_init
@dataclass
class PyArgument:
    '''
    一个python方法的参数, 可以是带有默认值的键值对参数, 也可以是普通参数
    '''
    name: str
    type_expr: PyTypeExpr
    default_value: PyValueExpr | None = field(default=None)
    
    @staticmethod
    def convert_to_string(argument: 'PyArgument') -> str:
        if argument.default_value:
            return f"{argument.name}: {PyTypeExpr.convert_to_string(argument.type_expr)} = {PyValueExpr.convert_to_string(argument.default_value)}"
        return f"{argument.name}: {PyTypeExpr.convert_to_string(argument.type_expr)}"
    
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
class PyMethod:
    '''
    一个python方法, 包含参数, 返回值, 是否是静态方法, 是否是可变长参数
    '''
    name: str
    description_lines: list[str] = field(default_factory=list)
    return_type_expr: PyTypeExpr | None = field(default=None)
    arguments: list[PyArgument] = field(default_factory=list)
    vararg_position: int | None = field(default=None)
    return_value: PyValueExpr | None = field(default=None)
    is_static: bool = False
    
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
        
        lines.append(f'def {method.name}({", ".join(args_expr)}) -> {return_type_expr}:')
        
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
class PyMember:
    '''
    一个python属性(赋值语句), 包含名称, 类型, 内联注释
    '''
    specified_string: str | None = field(default=None)  # 如果指定了字符串, 那么convert_to_string将直接返回这个字符串, 同时validate将返回True
    name: str | None = field(default=None)
    type_expr: PyTypeExpr | None = field(default=None)
    value_expr: PyValueExpr | None = field(default=None)
    inline_comment: str|None = field(default=None)
    
    @staticmethod
    def convert_to_string(member: 'PyMember') -> str:
        if member.specified_string is not None:
            return member.specified_string
        
        s = f'{member.name}: {PyTypeExpr.convert_to_string(member.type_expr)}'
        if member.value_expr:
            s += f' = {PyValueExpr.convert_to_string(member.value_expr)}'
        if member.inline_comment:
            s += f'  # {member.inline_comment}'
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
class PyClass:
    '''
    一个python类, 包含类型, 描述, 成员, 类属性, 方法
    '''
    type: PyType
    description_lines: list[str] = field(default_factory=list)
    
    members: list[PyMember] = field(default_factory=list)
    class_attributes: list[PyMember] = field(default_factory=list)
    methods: list[PyMethod] = field(default_factory=list)
    
    @staticmethod
    def _is_empty_class(pyclass: 'PyClass') -> bool:
        return not pyclass.members and not pyclass.class_attributes and not pyclass.methods

    @staticmethod
    def get_category(pyclass: 'PyClass') -> PyTypeCategory:
        return pyclass.type.category
    
    @staticmethod
    def convert_to_lines(pyclass: 'PyClass') -> list[str]:
        lines = []
        
        # class xxx(xxx):
        if pyclass.type.inherit:
            lines.append(f'class {PyType.convert_to_string(pyclass.type)}({PyType.convert_to_string(pyclass.type.inherit)}):')
        else:
            lines.append(f'class {PyType.convert_to_string(pyclass.type)}:')
        
        
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
            lines.append(PyMember.convert_to_string(member))
        lines.append('')
        
        # class methods
        for method in pyclass.methods:
            lines.extend(PyMethod.convert_to_lines(method))

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


@validate_types_on_init
@dataclass
class PyFile:
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
        for import_ in pyfile.imports:
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
        for pyclass in pyfile.classes:
            lines.extend(PyClass.convert_to_lines(pyclass))
            lines.append('')
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


