from dataclasses import dataclass, field
from enum import Enum
import re

DEBUG = True

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




class PyTypeCategory(Enum):
    PY_BUILTIN = "PY_BUILTIN"
    PY_GODOT_TYPE = "PY_GODOT_TYPE"
    PY_ENUM = "PY_ENUM"
    PY_SINGLETON = "PY_SINGLETON"



@dataclass
class PyType:
    '''
    一个python类型，可能是内置类型，也可能是godot类型，也可能是枚举类型
    '''
    name: str
    inherit: 'PyType' | None = field(default=None)
    category: PyTypeCategory
    
    @staticmethod
    def convert_to_string(type: 'PyType') -> str:
        if type.category == PyTypeCategory.PY_BUILTIN:
            return type.name
        elif type.category == PyTypeCategory.PY_GODOT_TYPE:
            return type.name
        elif type.category == PyTypeCategory.PY_ENUM:
            return type.name

    @staticmethod
    def validate(type: 'PyType') -> bool:
        results = ValidatorResults()
        results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', type.name)))
        return results.result()

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


@dataclass
class PyValueExpr:
    '''
    一个python值(字面量)
    '''
    value_expr: str
    type_expr: PyTypeExpr | None
    
    @staticmethod
    def convert_to_string(value: 'PyValueExpr') -> str:
        return value.value_expr
    
    @staticmethod
    def validate(value: 'PyValueExpr') -> bool:
        results = ValidatorResults()
        if value.type_expr:
            results.append(PyTypeExpr.validate(value.type_expr))
        return results.result()


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
        if argument.name:
            results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', argument.name)))
        else:
            results.append(False)
        return results.result()




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
    
    
    
    
@dataclass
class PyMember:
    '''
    一个python属性(赋值语句), 包含名称, 类型, 内联注释
    '''
    name: str
    type_expr: PyTypeExpr
    inline_comment: str = field(default="")
    
    @staticmethod
    def convert_to_string(member: 'PyMember') -> str:
        s = f'{member.name}: {PyTypeExpr.convert_to_string(member.type_expr)}'
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
            
        if member.name:
            results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', member.name)))
        else:
            results.append(False)
            
        return results.result()

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


