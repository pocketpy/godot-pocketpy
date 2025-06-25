from dataclasses import dataclass
from enum import Enum

class PyTypeCategory(Enum):
    PY_BUILTIN = "PY_BUILTIN"
    PY_GODOT_TYPE = "PY_GODOT_TYPE"
    PY_ENUM = "PY_ENUM"
    



@dataclass
class PyType:
    '''
    一个python类型，可能是内置类型，也可能是godot类型，也可能是枚举类型
    '''
    name: str
    inherit: 'PyType' | None = None
    category: PyTypeCategory
    
    @staticmethod
    def convert_to_string(type: 'PyType') -> str:
        if type.category == PyTypeCategory.PY_BUILTIN:
            return type.name
        elif type.category == PyTypeCategory.PY_GODOT_TYPE:
            return type.name
        elif type.category == PyTypeCategory.PY_ENUM:
            return type.name


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

@dataclass
class PyValue:
    '''
    一个python值(字面量)
    '''
    literal: str
    type: PyTypeExpr
    
    @staticmethod
    def convert_to_string(value: 'PyValue') -> str:
        return value.literal


@dataclass
class PyArgument:
    '''
    一个python方法的参数, 可以是带有默认值的键值对参数, 也可以是普通参数
    '''
    name: str
    type: PyType
    default_value: PyValue | None = None
    
    @staticmethod
    def convert_to_string(argument: 'PyArgument') -> str:
        if argument.default_value:
            return f"{argument.name}: {PyType.convert_to_string(argument.type)} = {PyValue.convert_to_string(argument.default_value)}"
        return f"{argument.name}: {PyType.convert_to_string(argument.type)}"




@dataclass
class PyMethod:
    '''
    一个python方法, 包含参数, 返回值, 是否是静态方法, 是否是可变长参数
    '''
    name: str
    description_lines: list[str] = []
    return_type: PyType | None = None
    arguments: list[PyArgument] = []
    vararg_position: int | None = None
    return_value: PyValue | None = None
    is_static: bool = False
    
    @staticmethod
    def convert_to_lines(method: 'PyMethod') -> list[str]:
        lines = []
        
        # @staticmethod
        if method.is_static:
            lines.append('@staticmethod')
        
        # def xxx(xxx: xxx, xxx: xxx, *args, xxx: xxx = xxx) -> xxx:
        args_expr = []
        for i,arg in enumerate(method.arguments):
            if i == method.vararg_position:
                args_expr.append('*args')
            else:
                args_expr.append(PyArgument.convert_to_string(arg))

        return_type_expr = PyType.convert_to_string(method.return_type) if method.return_type else "None"
        
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
    
@dataclass
class PyMember:
    name: str
    type: PyType
    inline_comment: str = ""
    
    @staticmethod
    def convert_to_string(member: 'PyMember') -> str:
        s = f'{member.name}: {PyType.convert_to_string(member.type)}'
        if member.inline_comment:
            s += f'  # {member.inline_comment}'
        return s


@dataclass
class PyClass:
    type: PyType
    description_lines: list[str] = []
    
    members: list[PyMember] = []
    class_attributes: list[PyMember] = []
    methods: list[PyMethod] = []
    
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



class PyFile:
    name: str
    
    imports: list[str] = []
    description_lines: list[str] = []
    
    global_variables: list[PyMember] = []
    global_functions: list[PyMethod] = []
    classes: list[PyClass] = []
    
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


