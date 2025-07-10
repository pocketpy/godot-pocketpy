from typing import Dict, List, Optional, Set, Tuple, Any
import re
from dataclasses import dataclass

from .schema_py import (
    PyType, PyTypeExpr, PyValueExpr,
    PyArgument, PyMethod, PyMember, PyClass, PyFile,
    SpecifiedPyMember
)
from .godot_types import (
    GodotTypeCategory, GodotTypeRegistry,
    GodotTypeParser, try_parse_operator_name
)
from .type_manager import TypeManager, TypeExprFactory
from ..schema_gdt import (
    GodotInOne, ClassesSingle, BuiltinClass,
    GlobalEnum, ClassesEnum, BuiltinClassEnum,
    ClassesProperty, ClassesConstant, BuiltinClassConstant,
    ClassesMethod, BuiltinClassMethod, ClassesMethodVirtual
)
from ..writer import Writer
from ..tools import DEBUG


def map_methods(cls_data: ClassesSingle | BuiltinClass, pyclass: PyClass) -> None:
    """
    映射方法，包括普通方法和静态方法
    
    Args:
        cls_data: Godot类数据
        pyclass: Python类对象
    """
    # 计算每个方法出现的次数, 用于判断是否需要@overload
    number_of_occurrences: Dict[str, int] = {}
    for method_data in cls_data.methods or []:
        if method_data.name in number_of_occurrences:
            number_of_occurrences[method_data.name] += 1
        else:
            number_of_occurrences[method_data.name] = 1

    # 添加方法
    for method_data in cls_data.methods or []:
        is_overload = number_of_occurrences[method_data.name] > 1
        is_required = False
        descriptions: List[str] = []
        if method_data.description:
            descriptions.append(method_data.description)
        if descriptions:
            description = '"""' + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()

        if isinstance(method_data, BuiltinClassMethod):
            return_type: Optional[str] = method_data.return_type
            py_return_type_expr = (
                TypeExprFactory.create_type_expr(return_type) if return_type else None
            )
        elif isinstance(method_data, ClassesMethod):
            return_type: Optional[str] = (
                method_data.return_value.type if method_data.return_value else None
            )
            py_return_type_expr = (
                TypeExprFactory.create_type_expr(return_type) if return_type else None
            )
        elif isinstance(method_data, ClassesMethodVirtual):
            is_required = False  # 虚方法有默认实现，不需要显式声明为@abstractmethod
            return_type: Optional[str] = (
                method_data.return_value.type if method_data.return_value else None
            )
            py_return_type_expr = (
                TypeExprFactory.create_type_expr(return_type) if return_type else None
            )
        else:
            raise ValueError(
                f"无效的类类型: {cls_data} 在映射方法时: {method_data}"
            )

        pyclass.methods.append(
            PyMethod(
                name=method_data.name,
                description_lines=descriptions,
                arguments=[],
                vararg_position=(
                    None
                    if not method_data.is_vararg or method_data.arguments is None
                    else len(method_data.arguments)
                ),
                return_type_expr=py_return_type_expr,
                is_static=method_data.is_static,
                is_overload=is_overload,
                is_required=is_required,
            )
        )

        map_method_arguments(method_data, pyclass.methods[-1])


def map_method_arguments(
    method_data: ClassesMethod | BuiltinClassMethod | ClassesMethodVirtual,
    pymethod: PyMethod,
) -> None:
    """
    映射方法参数
    
    Args:
        method_data: Godot方法数据
        pymethod: Python方法对象
    """
    for argument_data in method_data.arguments or []:
        pymethod.arguments.append(
            PyArgument(
                name=argument_data.name,
                type_expr=TypeExprFactory.create_type_expr(argument_data.type),
                default_value=(
                    PyValueExpr(
                        value_expr=argument_data.default_value,
                        type_expr=TypeExprFactory.create_type_expr(argument_data.type),
                    )
                    if argument_data.default_value
                    else None
                ),
            )
        )


def map_builtin_constants(
    constants: List[BuiltinClassConstant] | None, pyclass: PyClass
) -> None:
    """
    映射内置类常量/类属性
    
    Args:
        constants: Godot内置类常量列表
        pyclass: Python类对象
    """
    if not constants:
        return
    for const in constants:
        pyclass.members.append(
            PyMember(
                name=const.name,
                type_expr=TypeExprFactory.create_type_expr(str(const.type)),
                value_expr=PyValueExpr(
                    value_expr=str(const.value),
                    type_expr=TypeExprFactory.create_type_expr(str(const.type)),
                ),
                inline_comment=const.description,
            )
        )


def map_class_constants(
    constants: List[ClassesConstant] | None, pyclass: PyClass
) -> None:
    """
    映射类常量/类属性
    
    Args:
        constants: Godot类常量列表
        pyclass: Python类对象
    """
    if not constants:
        return
    for const in constants:
        pyclass.members.append(
            PyMember(
                name=const.name,
                type_expr=TypeExprFactory.create_type_expr("int"),
                value_expr=PyValueExpr(
                    value_expr=str(const.value),
                    type_expr=TypeExprFactory.create_type_expr("int"),
                ),
                inline_comment=const.description,
            )
        )


def map_signals(cls_data: ClassesSingle, pyclass: PyClass) -> None:
    """
    映射信号（特殊类型的类属性）
    
    Args:
        cls_data: Godot类数据
        pyclass: Python类对象
    """
    for signal_data in cls_data.signals or []:
        # 创建信号类型表达式
        colon = ":"
        # Signal(Callable((arg1_name:arg1_type|arg2_name:arg2_type|...), None))
        signal_type_expr = f"Signal(Callable(({'|'.join([arg.name + colon + arg.type for arg in signal_data.arguments or []])}), None))"
        
        # 处理信号描述
        if signal_data.description:
            replaced_description = signal_data.description.replace("\n", "    ")
        else:
            replaced_description = ""

        # 添加信号成员
        pyclass.members.append(
            PyMember(
                name=signal_data.name,
                type_expr=TypeExprFactory.create_type_expr(signal_type_expr),
                inline_comment=replaced_description,
            )
        )


def map_operators(cls_data: BuiltinClass, pyclass: PyClass) -> None:
    """
    映射运算符重载
    
    Args:
        cls_data: Godot内置类数据
        pyclass: Python类对象
    """
    # 计算每个运算符出现的次数, 用于判断是否需要@overload
    number_of_occurrences: Dict[str, int] = {}
    for operator_data in cls_data.operators or []:
        if operator_data.name in number_of_occurrences:
            number_of_occurrences[operator_data.name] += 1
        else:
            number_of_occurrences[operator_data.name] = 1

    # 添加运算符重载
    for operator_data in cls_data.operators or []:
        is_overload = number_of_occurrences[operator_data.name] > 1
        
        # 尝试解析操作符名
        python_operator_name = try_parse_operator_name(operator_data.name)
        if python_operator_name:
            if operator_data.right_type:
                # 二元运算符（如 __add__、__sub__ 等），有 right_type
                pyclass.methods.append(
                    PyMethod(
                        name=python_operator_name,
                        arguments=[
                            PyArgument(
                                name=operator_data.right_type,
                                type_expr=TypeExprFactory.create_type_expr(
                                    operator_data.right_type
                                ),
                            )
                        ],
                        return_type_expr=TypeExprFactory.create_type_expr(
                            operator_data.return_type
                        ),
                        description_lines=(
                            operator_data.description.splitlines()
                            if operator_data.description
                            else []
                        ),
                        is_overload=is_overload,
                    )
                )
            else:
                # 一元运算符（如 __neg__、__invert__ 等），没有 right_type
                pyclass.methods.append(
                    PyMethod(
                        name=python_operator_name,
                        arguments=[],
                        return_type_expr=TypeExprFactory.create_type_expr(
                            operator_data.return_type
                        ),
                        description_lines=(
                            operator_data.description.splitlines()
                            if operator_data.description
                            else []
                        ),
                        is_overload=is_overload,
                    )
                )
        else:
            if DEBUG:
                print(
                    f"警告: 不支持的运算符: '{operator_data.name}' 在 '{cls_data.name}' 中"
                )


def map_enum(
    enum_data: GlobalEnum | ClassesEnum | BuiltinClassEnum, pyclass: PyClass
) -> None:
    """
    映射枚举类型
    
    Args:
        enum_data: Godot枚举数据
        pyclass: Python类对象
    """
    for enum_value_data in enum_data.values or []:
        pyclass.class_attributes.append(
            PyMember(
                name=enum_value_data.name,
                type_expr=TypeExprFactory.create_type_expr("int"),
                value_expr=PyValueExpr(
                    value_expr=str(enum_value_data.value),
                    type_expr=TypeExprFactory.create_type_expr("int"),
                ),
                inline_comment=enum_value_data.description,
            )
        )


def map_class_properties(
    properties: List[ClassesProperty] | None, pyclass: PyClass
) -> None:
    """
    映射类属性/成员变量
    
    Args:
        properties: Godot类属性列表
        pyclass: Python类对象
    """
    if not properties:
        return
    for member_data in properties:
        pyclass.members.append(
            PyMember(
                name=member_data.name,
                type_expr=TypeExprFactory.create_type_expr(member_data.type),
                inline_comment=member_data.description,
            )
        )


@dataclass
class MapResult:
    """映射结果"""
    typings_pyi: PyFile
    enum_pyi: PyFile
    init_pyi: PyFile
    c_writer: Writer


def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> MapResult:
    """
    主映射函数，将Godot类型映射到Python类型
    
    Args:
        gdt_all_in_one: Godot类型定义
        
    Returns:
        MapResult: 映射结果
    """
    # 初始化类型系统
    TypeManager.build_type_sets(gdt_all_in_one)

    # 创建映射结果
    map_result = MapResult(
        typings_pyi=PyFile(
            name="typings.pyi",
            imports=[
                """import typing""",
                """from typing import overload, abstractmethod""",
                "from .enum import *",
                "",
                "",
                "def default(gdt_expr: str) -> typing.Any: ...",
            ],
            classes=[],
        ),
        enum_pyi=PyFile(
            name="enum.pyi",
            imports=["""from enum import Enum"""],
            classes=[],
        ),
        init_pyi=PyFile(
            name="__init__.pyi",
            imports=[
                "from . import typings as _typings",
                "",
                "",
                "class GDNativeSingleton[T: _typings.Object]:",
                "    def __init__(self, name: str): ...",
                "",
                "class GDNativeClass[T: _typings.Variant]:",
                "    def __init__(self, name: str): ...",
                "",
                "class Script[T: _typings.Object]:",
                "    @property",
                "    def owner(self) -> T: ...",
                "",
                "def Extends[T: _typings.Object](cls: GDNativeClass[T]) -> type[Script[T]]: ...",
            ],
            global_variables=[],
        ),
        c_writer=Writer(),
    )

    # 初始化C++代码生成器
    c_writer = map_result.c_writer
    c_writer.write('#include "Bindings.hpp"')

    # 导入单例类型的头文件
    for pytype in PyType.ALL_TYPES.values():
        if GodotTypeRegistry.get_category(pytype) == GodotTypeCategory.SINGLETON_GODOT_NATIVE:
            if pytype.name == "ClassDB":
                # TODO: implement ClassDB singleton
                continue
            s1 = re.sub("(.)([A-Z][a-z0-9]+)", r"\1_\2", pytype.name)
            header_name = re.sub("([a-z])([A-Z])", r"\1_\2", s1).lower()
            c_writer.write(f"#include <godot_cpp/classes/{header_name}.hpp>")

    c_writer.write("")
    c_writer.write("namespace pkpy {")
    c_writer.write("")
    c_writer.write("void setup_bindings_generated() {")
    c_writer.indent()

    # 映射单一类
    class_single_classes: List[PyClass] = []
    for cls_data in gdt_all_in_one.classes:
        descriptions: List[str] = []
        if cls_data.brief_description:
            descriptions.append(cls_data.brief_description)
        if cls_data.description:
            descriptions.append(cls_data.description)
        if descriptions:
            description = '"""' + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
        
        pyclass = PyClass(
            type=TypeManager.get_type(cls_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        # 处理各种属性
        map_class_properties(cls_data.properties, pyclass)
        map_methods(cls_data, pyclass)
        map_class_constants(cls_data.constants, pyclass)
        map_signals(cls_data, pyclass)
        class_single_classes.append(pyclass)

    # 映射内置类
    builtin_classes: List[PyClass] = []
    for cls_data in gdt_all_in_one.builtin_classes:
        descriptions: List[str] = []
        if cls_data.brief_description:
            descriptions.append(cls_data.brief_description)
        if cls_data.description:
            descriptions.append(cls_data.description)
        if descriptions:
            description = '"""' + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
        
        pyclass = PyClass(
            type=TypeManager.get_type(cls_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        # 处理各种属性
        map_methods(cls_data, pyclass)
        map_builtin_constants(cls_data.constants, pyclass)
        map_operators(cls_data, pyclass)
        builtin_classes.append(pyclass)

    # 映射全局枚举
    enum_classes = []
    for enum_data in gdt_all_in_one.global_enums:
        descriptions: List[str] = []
        if enum_data.description:
            descriptions.append(enum_data.description)
        if descriptions:
            description = '"""' + "\n" + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()

        pyclass = PyClass(
            type=TypeManager.get_type(enum_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )

        map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)

    map_result.enum_pyi.classes.extend(enum_classes)

    # 映射类枚举
    folded_enums = [(cls_data.name, cls_data.enums) for cls_data in gdt_all_in_one.classes]
    flattened_enums = [
        (cls_name, enum_data)
        for cls_name, enums in folded_enums
        for enum_data in enums or []
    ]

    enum_classes = []
    for cls_name, enum_data in flattened_enums:
        descriptions: List[str] = []
        if enum_data.description:
            descriptions.append(enum_data.description)
        if descriptions:
            description = '"""' + "\n" + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()

        pyclass = PyClass(
            type=TypeManager.get_type(cls_name + "__" + enum_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )

        map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)

    map_result.enum_pyi.classes.extend(enum_classes)

    # 映射内置类枚举
    folded_enums = [
        (cls_data.name, cls_data.enums) for cls_data in gdt_all_in_one.builtin_classes
    ]
    flattened_enums = [
        (cls_name, enum_data)
        for cls_name, enums in folded_enums
        for enum_data in enums or []
    ]
    
    enum_classes = []
    for cls_name, enum_data in flattened_enums:
        descriptions: List[str] = []
        if enum_data.description:
            descriptions.append(enum_data.description)
        if descriptions:
            description = '"""' + "\n" + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()

        pyclass = PyClass(
            type=TypeManager.get_type(cls_name + "__" + enum_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
            
        map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)

    map_result.enum_pyi.classes.extend(enum_classes)

    # 处理初始化文件内容
    for pytype in PyType.ALL_TYPES.values():
        if GodotTypeRegistry.get_category(pytype) == GodotTypeCategory.SINGLETON_GODOT_NATIVE:
            map_result.init_pyi.global_variables.append(
                SpecifiedPyMember(
                    specified_string=f"{pytype.name} = GDNativeSingleton[_typings.{pytype.name}]('{pytype.name}')",
                )
            )
            if pytype.name == "ClassDB":
                # TODO: implement ClassDB singleton
                continue
            c_writer.write(
                f'register_GDNativeSingleton("{pytype.name}", {pytype.name}::get_singleton());'
            )

    c_writer.write("")
    for pytype in PyType.ALL_TYPES.values():
        if GodotTypeRegistry.get_category(pytype) == GodotTypeCategory.GODOT_NATIVE:
            map_result.init_pyi.global_variables.append(
                SpecifiedPyMember(
                    specified_string=f"{pytype.name} = GDNativeClass[_typings.{pytype.name}]('{pytype.name}')",
                )
            )
            c_writer.write(f'register_GDNativeClass("{pytype.name}");')

    # 添加类到typings.pyi
    for class_single_class in class_single_classes:
        map_result.typings_pyi.classes.append(class_single_class)

    for builtin_class in builtin_classes:
        map_result.typings_pyi.classes.append(builtin_class)

    # Variant类型
    pyclass = PyClass(
        type=TypeManager.get_type("Variant"),
        description_lines=[],
        members=[],
        class_attributes=[],
        methods=[],
    )
    map_result.typings_pyi.classes.append(pyclass)

    # intptr类型
    map_result.typings_pyi.global_variables.append(
        SpecifiedPyMember(
            specified_string="intptr = int",
            inline_comment="intptr is a pointer to an unknown type (const void*)",
        )
    )

    # 完成C++代码生成
    c_writer.dedent()
    c_writer.write("}")
    c_writer.write("")
    c_writer.write("} // namespace pkpy")

    return map_result 