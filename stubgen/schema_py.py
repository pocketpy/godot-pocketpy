from dataclasses import dataclass, field, fields
from enum import Enum
import re
from typing import Any, get_origin, get_args

DEBUG = True


def validate_types_on_init(cls):
    original_init = cls.__init__
    
    def __init__(self: Any, *args: Any, **kwargs: Any) -> None:
        original_init(self, *args, **kwargs)
        for field in fields(cls):
            value = getattr(self, field.name)
            field_type = field.type
            
            # 获取基础类型和泛型参数
            origin_type = get_origin(field_type)
            type_args = get_args(field_type)
            
            # 检查基础类型
            check_type = origin_type if origin_type is not None else field_type
            
            # 跳过Any类型的检查
            if check_type == Any:
                continue
                
            # 检查值是否为正确的基础类型
            if not isinstance(value, check_type):
                raise TypeError(f"Expected {field.name} to be {field_type}, got {type(value)}")
            
            # 如果是容器类型且有类型参数，检查内部元素
            if type_args and hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
                # 对列表、集合等可迭代对象的每个元素进行类型检查
                for i, item in enumerate(value):
                    if not isinstance(item, type_args[0]):
                        raise TypeError(f"Item {i} in {field.name} expected to be {type_args[0]}, got {type(item)}")
            
            # 对字典类型的特殊处理
            elif type_args and isinstance(value, dict) and len(type_args) == 2:
                for k, v in value.items():
                    if not isinstance(k, type_args[0]):
                        raise TypeError(f"Dict key in {field.name} expected to be {type_args[0]}, got {type(k)}")
                    if not isinstance(v, type_args[1]):
                        raise TypeError(f"Dict value for key {k} in {field.name} expected to be {type_args[1]}, got {type(v)}")
    
    cls.__init__ = __init__
    return cls


class ValidatorResults():
    def __init__(self) -> None:
        self.results = []
    
    def append(self, result: bool) -> None:
        if DEBUG:
            if not result:
                raise ValueError(f"Validation failed")
        
        self.results.append(result)
        
    def result(self) -> bool:
        return all(self.results)




class _PyTypeCategory(Enum):
    CAN_TRANSFER_TO_PY_BUILTIN = "CAN_TRANSFER_TO_PY_BUILTIN"
    GODOT_NATIVE = "GODOT_NATIVE"
    ENUM = "ENUM"
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
    name: str
    _category: _PyTypeCategory = field(default=None, init=False)
    inherit: 'PyType' | None = field(default=None)
    
    
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
    BUILTIN_TYPES = {"Nil":'None', "int":'int', "float":'float', "bool":'bool', "String":'str'}
    SINGLETON_TYPES: set['PyType']
    NOT_SINGLETON_TYPES: set['PyType']
    
    @classmethod
    def add_singleton_type(cls, pytype: 'PyType') -> None:
        if cls.SINGLETON_TYPES is None:
            cls.SINGLETON_TYPES = set()
        cls.SINGLETON_TYPES.add(pytype)
    @classmethod
    def add_not_singleton_type(cls, pytype: 'PyType') -> None:
        if cls.NOT_SINGLETON_TYPES is None:
            cls.NOT_SINGLETON_TYPES = set()
        cls.NOT_SINGLETON_TYPES.add(pytype)

    @staticmethod
    def is_singleton(pytype: 'PyType') -> bool:
        if pytype not in PyType.SINGLETON_TYPES and pytype not in PyType.NOT_SINGLETON_TYPES:
            raise ValueError(f"Singleton type not found: {pytype.name}")
        
        if pytype in PyType.SINGLETON_TYPES:
            return True
        return False
    
    def __post_init__(self) -> None:
        self.name = PyType.try_parse_name(self.name)
        
        if self.name in PyType.BUILTIN_TYPES:
            self._category = PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN
            
        elif self.name.startswith('enum::'):
            self._category = PyTypeCategory.ENUM
            
        else:
            self._category = PyTypeCategory.GODOT_NATIVE
        
    @property
    def category(self) -> PyTypeCategory:
        if self._category == _PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN:
            return PyTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN
        elif self._category == _PyTypeCategory.GODOT_NATIVE:
            if PyType.is_singleton(self):
                return PyTypeCategory.SINGLETON_GODOT_NATIVE
            else:
                return PyTypeCategory.GODOT_NATIVE
        elif self._category == _PyTypeCategory.ENUM:
            return PyTypeCategory.ENUM
        else:
            raise ValueError(f"Invalid type: {self.name}")
    
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
        elif type.category == PyTypeCategory.SINGLETON:
            return type.name
        else:
            raise ValueError(f"Invalid type: {type.name}")
        
    @staticmethod
    def validate(type: 'PyType') -> bool:
        results = ValidatorResults()
        results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', type.name)))
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
    def try_parse_name(name: str) -> str|None:
        
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
    name: str
    type_expr: PyTypeExpr
    value_expr: PyValueExpr | None = field(default=None)
    inline_comment: str = field(default="")
    
    @staticmethod
    def convert_to_string(member: 'PyMember') -> str:
        s = f'{member.name}: {PyTypeExpr.convert_to_string(member.type_expr)}'
        if member.value_expr:
            s += f' = {PyValueExpr.convert_to_string(member.value_expr)}'
        if member.inline_comment:
            s += f'  # {member.inline_comment}'
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
class PyClass:
    '''
    一个python类, 包含类型, 描述, 成员, 类属性, 方法
    '''
    type_expr: PyTypeExpr
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
            lines.append(f'class {PyType.convert_to_string(pyclass.type)}({PyType.convert_to_string(pyclass.inherit)}):')
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


