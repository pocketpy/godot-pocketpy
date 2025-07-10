from typing import Dict, List, Literal, Optional, Set, Tuple, Union, Any
from keyword import iskeyword

from .schema_py import (
    PyType, PyTypeExpr, PyValueExpr, 
    PyArgument, PyMethod, PyMember, 
    SpecifiedPyMember, PyClass, PyFile
)
from .godot_types import (
    GodotTypeRegistry, GodotValueCategory,
    map_godot_value_category, GODOT_OPERATORS_TABLE
)
from .type_manager import TypeManager


class CodeGenerator:
    """
    代码生成器 - 负责生成Python代码
    """
    
    @staticmethod
    def convert_type_to_string(pytype: PyType, wrap_with_single_quote: bool = True) -> str:
        """
        将类型转换为字符串表示
        
        Args:
            pytype: 要转换的类型
            wrap_with_single_quote: 是否用单引号包围
            
        Returns:
            str: 类型的字符串表示
        """
        if wrap_with_single_quote:
            return "'" + pytype.name + "'" 
        else:
            return pytype.name
    
    @staticmethod
    def convert_type_expr_to_string(pytype_expr: PyTypeExpr, wrap_with_single_quote: bool = True) -> str:
        """
        将类型表达式转换为字符串表示
        
        Args:
            pytype_expr: 要转换的类型表达式
            wrap_with_single_quote: 是否用单引号包围
            
        Returns:
            str: 类型表达式的字符串表示
        """
        if wrap_with_single_quote:
            return "'" + pytype_expr.expr_str + "'"
        else:
            return pytype_expr.expr_str
    
    @staticmethod
    def convert_value_expr_to_string(pyvalue: PyValueExpr) -> str:
        """
        将值表达式转换为字符串表示
        
        Args:
            pyvalue: 要转换的值表达式
            
        Returns:
            str: 值表达式的字符串表示
        """
        if pyvalue.type_expr is None:
            return f"default({repr(pyvalue.value_expr)})"
        
        # 获取值分类
        value_category = map_godot_value_category(pyvalue.value_expr, pyvalue.type_expr, GodotTypeRegistry)
        
        if value_category == GodotValueCategory.NULL:
            return 'None'
        elif value_category == GodotValueCategory.INT:
            return pyvalue.value_expr
        elif value_category == GodotValueCategory.FLOAT:
            return pyvalue.value_expr
        elif value_category == GodotValueCategory.STR:
            return pyvalue.value_expr
        elif value_category == GodotValueCategory.BOOL:
            if pyvalue.value_expr.lower() == 'true':
                return 'True'
            elif pyvalue.value_expr.lower() == 'false':
                return 'False'
            else:
                raise ValueError(f"无效的布尔值: {pyvalue.value_expr}")
        elif value_category == GodotValueCategory.ENUM_CONST:
            # 枚举值需要特殊处理，此处暂时简单实现
            return f"default({repr(pyvalue.value_expr)})"
        else:
            return f"default({repr(pyvalue.value_expr)})"
    
    @staticmethod
    def convert_argument_to_string(argument: PyArgument, wrap_with_single_quote: bool = True) -> str:
        """
        将参数转换为字符串表示
        
        Args:
            argument: 要转换的参数
            wrap_with_single_quote: 是否用单引号包围类型
            
        Returns:
            str: 参数的字符串表示
        """
        # 处理Python关键字
        keyword_underline = ""
        if iskeyword(argument.name):
            keyword_underline = "_"
        
        # 构建参数字符串
        if argument.default_value:
            return f"{argument.name}{keyword_underline}: {CodeGenerator.convert_type_expr_to_string(argument.type_expr, wrap_with_single_quote)} = {CodeGenerator.convert_value_expr_to_string(argument.default_value)}"
        else:
            return f"{argument.name}{keyword_underline}: {CodeGenerator.convert_type_expr_to_string(argument.type_expr, wrap_with_single_quote)}"
    
    @staticmethod
    def convert_member_to_string(member: PyMember, type_annotation_mode: Literal['explicit', 'comment', 'none'] = 'explicit', wrap_with_single_quote: bool = True) -> str:
        """
        将成员（属性）转换为字符串表示
        
        Args:
            member: 要转换的成员
            type_annotation_mode: 类型注解模式 ('explicit'=显式注解, 'comment'=注释形式, 'none'=无注解)
            wrap_with_single_quote: 是否用单引号包围类型
            
        Returns:
            str: 成员的字符串表示
        """
        # 处理Python关键字
        keyword_underline = ""
        if iskeyword(member.name):
            keyword_underline = "_"
        
        # 构建基本成员字符串
        s = f'{member.name}{keyword_underline}'
        
        # 添加类型注解
        if type_annotation_mode == "explicit":
            s += f": {CodeGenerator.convert_type_expr_to_string(member.type_expr, wrap_with_single_quote)}"
        
        # 添加值
        if member.value_expr:
            s += f' = {CodeGenerator.convert_value_expr_to_string(member.value_expr)}'
        
        # 添加注释
        if type_annotation_mode == "comment" or member.inline_comment:
            comment_parts = []
            
            # 只有comment模式才会添加类型注解到注释中
            if type_annotation_mode == "comment":
                comment_parts.append(f"type: {CodeGenerator.convert_type_expr_to_string(member.type_expr, wrap_with_single_quote)}")
            
            # 无论何种模式下，若存在inline_comment，那么都显示内联注释
            if member.inline_comment:
                comment_parts.append(f"comment: {member.inline_comment}")
            
            if comment_parts:
                s += f"  # {' '.join(comment_parts)}"
        
        return s
    
    @staticmethod
    def convert_specified_member_to_string(specified_py_member: SpecifiedPyMember) -> str:
        """
        将指定的成员转换为字符串表示
        
        Args:
            specified_py_member: 要转换的指定成员
            
        Returns:
            str: 成员的字符串表示
        """
        s = specified_py_member.specified_string
        if specified_py_member.inline_comment:
            s += f"  # {specified_py_member.inline_comment}"
        return s
    
    @staticmethod
    def convert_method_to_lines(method: PyMethod, wrap_with_single_quote: bool = True) -> List[str]:
        """
        将方法转换为代码行
        
        Args:
            method: 要转换的方法
            wrap_with_single_quote: 是否用单引号包围类型
            
        Returns:
            List[str]: 方法的代码行列表
        """
        lines: List[str] = []
        
        # 添加装饰器
        if method.is_static:
            lines.append('@staticmethod')
        
        if method.is_overload:
            lines.append('@overload')
        
        if method.is_required:
            lines.append('@abstractmethod')
        
        # 处理方法参数
        args_expr: List[str] = []
        if not method.is_static:
            args_expr.append('self')
            
        for i, arg in enumerate(method.arguments):
            if i == method.vararg_position:
                args_expr.append('*args')
            else:
                args_expr.append(CodeGenerator.convert_argument_to_string(arg, wrap_with_single_quote=wrap_with_single_quote))
        
        # 添加返回类型
        return_type_expr = CodeGenerator.convert_type_expr_to_string(method.return_type_expr, wrap_with_single_quote) if method.return_type_expr else "None"
        
        # 处理Python关键字
        keyword_underline = ""
        if iskeyword(method.name):
            keyword_underline = "_"
        
        # 添加方法签名
        lines.append(f'def {method.name}{keyword_underline}({", ".join(args_expr)}) -> {return_type_expr}:')
        
        # 添加方法文档字符串和实现
        if method.description_lines:
            lines.extend([f'    {line}' for line in method.description_lines])
            lines.append('    ...')
        else:
            lines[-1] += ' ...'
        
        return lines
    
    @staticmethod
    def is_empty_class(pyclass: PyClass) -> bool:
        """
        检查类是否为空（无成员、属性和方法）
        
        Args:
            pyclass: 要检查的类
            
        Returns:
            bool: 如果类为空则为True，否则为False
        """
        return not pyclass.members and not pyclass.class_attributes and not pyclass.methods
    
    @staticmethod
    def convert_class_to_lines(pyclass: PyClass, wrap_with_single_quote: bool = True) -> List[str]:
        """
        将类转换为代码行
        
        Args:
            pyclass: 要转换的类
            wrap_with_single_quote: 是否用单引号包围类型
            
        Returns:
            List[str]: 类的代码行列表
        """
        lines: List[str] = []
        
        # 检查是否是需要忽略的类
        class_name = pyclass.type.name
        if class_name in PyClass.CLASS_IGNORED:
            return []
        
        # 处理类名别名
        if class_name in PyClass.CLASS_NAME_ALIAS:
            class_name = PyClass.CLASS_NAME_ALIAS[class_name]
        
        # 生成类定义
        GENERIC_TYPES = {
            "Signal": "[T: typing.Callable]",
            "Callable": "[T, R]",
            "Array": "[T]",
        }
        generic_annotation = GENERIC_TYPES.get(class_name, "")
        
        # 添加继承
        inherit_annotation = ""
        if pyclass.type.inherit:
            inherit_annotation = f'({CodeGenerator.convert_type_to_string(pyclass.type.inherit, wrap_with_single_quote)})'
        
        # 生成类定义行
        class_definition_line = f'class {class_name}{generic_annotation}{inherit_annotation}:'
        lines.append(class_definition_line)
        
        # 处理空类
        if CodeGenerator.is_empty_class(pyclass) and not pyclass.description_lines:
            lines[-1] += ' ...'
            return lines
        
        # 添加类文档字符串
        if pyclass.description_lines:
            lines.extend([f'    {line}' for line in pyclass.description_lines])
            
            # 处理空类（有文档但无内容）
            if CodeGenerator.is_empty_class(pyclass):
                lines.append('    ...')
                return lines
        
        # 添加类属性
        enum_type = GodotTypeRegistry.get_category(pyclass.type) == GodotValueCategory.ENUM
        
        if not enum_type:
            # 非枚举类型的类属性用注释形式显示类型
            for member in pyclass.class_attributes:
                lines.append("    " + CodeGenerator.convert_member_to_string(
                    member, 
                    type_annotation_mode='comment', 
                    wrap_with_single_quote=wrap_with_single_quote
                ))
        else:
            # 枚举类型不显示类型注解
            for member in pyclass.class_attributes:
                lines.append("    " + CodeGenerator.convert_member_to_string(
                    member, 
                    type_annotation_mode='none', 
                    wrap_with_single_quote=wrap_with_single_quote
                ))
        
        # 添加实例成员
        for member in pyclass.members:
            lines.append("    " + CodeGenerator.convert_member_to_string(
                member,
                wrap_with_single_quote=wrap_with_single_quote
            ))
        
        # 添加方法
        for method in pyclass.methods:
            if method.name in PyClass.METHOD_IGNORED:
                continue
            method_lines = CodeGenerator.convert_method_to_lines(method, wrap_with_single_quote)
            lines.extend([f'    {line}' for line in method_lines])
        
        return lines
    
    @staticmethod
    def convert_file_to_lines(pyfile: PyFile, wrap_with_single_quote: bool = True) -> List[str]:
        """
        将文件转换为代码行
        
        Args:
            pyfile: 要转换的文件
            wrap_with_single_quote: 是否用单引号包围类型
            
        Returns:
            List[str]: 文件的代码行列表
        """
        lines: List[str] = []
        
        # 添加导入语句
        lines.extend(pyfile.imports)
        lines.append('')
        lines.append('')
        
        # 添加文件文档字符串
        if pyfile.description_lines:
            lines.extend(pyfile.description_lines)
            lines.append('')
            lines.append('')
        
        # 添加全局变量
        for variable in pyfile.global_variables:
            if isinstance(variable, PyMember):
                if variable.name in PyFile.IGNORED_GLOBAL_VARIABLES:
                    continue
                lines.append(CodeGenerator.convert_member_to_string(variable, wrap_with_single_quote=wrap_with_single_quote))
            elif isinstance(variable, SpecifiedPyMember):
                if variable.specified_string.split('=')[0].strip() in PyFile.IGNORED_GLOBAL_VARIABLES:
                    continue
                lines.append(CodeGenerator.convert_specified_member_to_string(variable))
            lines.append('')
        
        # 添加全局函数
        for function in pyfile.global_functions:
            lines.extend(CodeGenerator.convert_method_to_lines(function, wrap_with_single_quote))
            lines.append('')
        
        # 添加类
        for pyclass in pyfile.classes:
            class_lines = CodeGenerator.convert_class_to_lines(pyclass, wrap_with_single_quote)
            if class_lines:  # 只有当类不被忽略时才添加
                lines.extend(class_lines)
                lines.append('')
                lines.append('')
        
        return lines 