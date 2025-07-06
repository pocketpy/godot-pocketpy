from .schema_gdt import *
from .schema_py import *
from .writer import Writer



# ===============================
# MARK: 通用映射
# ===============================


def _map_methods(cls_data: ClassesSingle|BuiltinClass, pyclass: PyClass) -> None:
    """映射方法，包括普通方法和静态方法"""
    
    # 计算每个方法出现的次数, 用于判断是否需要@overload
    number_of_occurrences: dict[str, int] = {}
    for method_data in cls_data.methods or []:
        if method_data.name in number_of_occurrences:
            number_of_occurrences[method_data.name] += 1
        else:
            number_of_occurrences[method_data.name] = 1
    
    # 添加方法
    for method_data in cls_data.methods or []:
        is_overload = number_of_occurrences[method_data.name] > 1
        descriptions: list[str] = []
        if method_data.description:
            descriptions.append(method_data.description)
        if descriptions:
            description = '"""' + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
        
        if isinstance(method_data, BuiltinClassMethod):
            return_type: str|None = method_data.return_type
            py_return_type_expr = PyTypeExpr.get_and_add(return_type) if return_type else None
        elif isinstance(method_data, ClassesMethod):
            return_type: str|None = method_data.return_value.type if method_data.return_value else None
            py_return_type_expr = PyTypeExpr.get_and_add(return_type) if return_type else None
        else:
            raise ValueError(f"Invalid class type: {cls_data}")
        
        
        pyclass.methods.append(PyMethod(
            name=method_data.name,
            description_lines=descriptions,
            arguments=[],
            vararg_position=None if not method_data.is_vararg or method_data.arguments is None else len(method_data.arguments),
            return_type_expr=py_return_type_expr,
            is_static=method_data.is_static,
            is_overload=is_overload,
        ))
        
        _map_method_arguments(method_data, pyclass.methods[-1])

def _map_method_arguments(method_data: ClassesMethod | BuiltinClassMethod | ClassesMethodVirtual, pymethod: PyMethod) -> None:
    """映射方法参数"""
    for argument_data in method_data.arguments or []:
        pymethod.arguments.append(PyArgument(
            name=argument_data.name,
            type_expr=PyTypeExpr.get_and_add(argument_data.type),
            default_value=PyValueExpr(
                value_expr=argument_data.default_value,
                type_expr=PyTypeExpr.get_and_add(argument_data.type),
            ) if argument_data.default_value else None,
        ))


# ===============================
# MARK: 各自独有的映射
# ===============================

def _map_builtin_constants(constants: list[BuiltinClassConstant] | None, pyclass: PyClass) -> None:
    """映射 BuiltinClassConstant 类型的类常量/类属性"""
    if not constants:
        return
    for const in constants:
        pyclass.members.append(
            PyMember(
                name=const.name,
                type_expr=PyTypeExpr.get_and_add(str(const.type)),
                value_expr=PyValueExpr(
                    value_expr=str(const.value),
                    type_expr=PyTypeExpr.get_and_add(str(const.type)),
                ),
                inline_comment=const.description,
            )
        )

def _map_class_constants(constants: list[ClassesConstant] | None, pyclass: PyClass) -> None:
    """映射 ClassesConstant 类型的类常量/类属性"""
    if not constants:
        return
    for const in constants:
        pyclass.members.append(
            PyMember(
                name=const.name,
                type_expr=PyTypeExpr.get_and_add("int"),
                value_expr=PyValueExpr(
                    value_expr=str(const.value),
                    type_expr=PyTypeExpr.get_and_add("int"),
                ),
                inline_comment=const.description,
            )
        )



def _map_signals(cls_data: ClassesSingle, pyclass: PyClass) -> None:
    """映射信号（特殊类型的类属性）"""
    for signal_data in cls_data.signals or []:
        # 创建信号类型表达式
        arg_types: list[PyTypeExpr] = []
        arg_comments: list[str] = []
        
        for arg in signal_data.arguments or []:
            arg_types.append(PyTypeExpr.get_and_add(arg.type))
            arg_comments.append(f"{arg.name}: {arg.type}")
        
        # 创建信号类型表达式
        signal_type_expr = f"Signal(Callable(({'|'.join([PyTypeExpr.convert_to_string(arg_type, wrap_with_single_quote=False) for arg_type in arg_types])}), None))"
        
        # 添加信号成员
        if signal_data.description:
            replaced_description = signal_data.description.replace('\n', '    ')
        else:
            replaced_description = ""
            
        pyclass.members.append(PyMember(
            name=signal_data.name,
            type_expr=PyTypeExpr.get_and_add(signal_type_expr),
            inline_comment=replaced_description
        ))
        
def _map_operators(cls_data: BuiltinClass, pyclass: PyClass) -> None:
    """映射运算符重载"""
    
    # 计算每个运算符出现的次数, 用于判断是否需要@overload
    number_of_occurrences: dict[str, int] = {}
    for operator_data in cls_data.operators or []:
        if operator_data.name in number_of_occurrences:
            number_of_occurrences[operator_data.name] += 1
        else:
            number_of_occurrences[operator_data.name] = 1
    
    # 添加运算符重载
    for operator_data in cls_data.operators or []:
        is_overload = number_of_occurrences[operator_data.name] > 1
        
        if PyMethod.try_parse_name(operator_data.name):
            
            if operator_data.right_type:
                # 二元运算符（如 __add__、__sub__ 等），有 right_type
                pyclass.methods.append(PyMethod(
					name=PyMethod.OPERATORS_TABLE[operator_data.name],
					arguments=[PyArgument(
					name=operator_data.right_type,
					type_expr=PyTypeExpr.get_and_add(operator_data.right_type),
					)],
					return_type_expr=PyTypeExpr.get_and_add(operator_data.return_type),
					description_lines=operator_data.description.splitlines() if operator_data.description else [],
                    is_overload=is_overload,
				))
            else:
                # 一元运算符（如 __neg__、__invert__ 等），没有 right_type
                pyclass.methods.append(PyMethod(
                    name=PyMethod.OPERATORS_TABLE[operator_data.name],
                    arguments=[],
                    return_type_expr=PyTypeExpr.get_and_add(operator_data.return_type),
                    description_lines=operator_data.description.splitlines() if operator_data.description else [],
                    is_overload=is_overload,
                ))
        else:
            if DEBUG:
                print(f"Warning: 不支持的运算符: '{operator_data.name}' 在 '{cls_data.name}' ")

def _map_enum(enum_data: GlobalEnum|ClassesEnum|BuiltinClassEnum, pyclass: PyClass) -> None:
    """映射枚举类型"""
    for enum_value_data in enum_data.values or []:
        pyclass.class_attributes.append(PyMember(
            name=enum_value_data.name,
            type_expr=PyTypeExpr.get_and_add('int'),
            value_expr=PyValueExpr(
                value_expr=str(enum_value_data.value),
                type_expr=PyTypeExpr.get_and_add('int'),
            ),
            inline_comment=enum_value_data.description,
        ))



def _map_class_properties(properties: list[ClassesProperty] | None, pyclass: PyClass) -> None:
    """映射 ClassesProperty 类型的实例属性/成员变量"""
    if not properties:
        return
    for member_data in properties:
        pyclass.members.append(PyMember(
            name=member_data.name,
            type_expr=PyTypeExpr.get_and_add(member_data.type),
            inline_comment=member_data.description,
        ))

# ===============================
# 入口
# ===============================

@dataclass
class MapResult:
    typings_pyi: PyFile
    enum_pyi: PyFile
    init_pyi: PyFile
    c_writer: Writer
    
    
def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> MapResult:
    PyType.build_type_sets(gdt_all_in_one)
    
    map_result = MapResult(
        typings_pyi=PyFile(
            name="typings.pyi",
            imports=[
            
            '''import typing''',
            '''from typing import overload''',
            'from .enum import *',
            "",
            "",
            'def default(gdt_expr: str) -> typing.Any: ...',
            ],
            classes=[],
        ),
        enum_pyi=PyFile(
            name="enum.pyi",
            imports=[
            '''from enum import Enum'''
            ],
            classes=[],
        ),
        init_pyi=PyFile(
            name="__init__.pyi",
            imports=[
            'from . import typings as _typings',
            '',
            '',
            'class GDNativeSingleton[T: _typings.Object]:',
            '    def __init__(self, name: str): ...',
            '',
            'class GDNativeClass[T: _typings.Variant]:',
            '    def __init__(self, name: str): ...',
            '',
            'class Script[T: _typings.Object]:',
            '    @property',
            '    def owner(self) -> T: ...',
            '',
            'def Extends[T: _typings.Object](cls: GDNativeClass[T]) -> type[Script[T]]: ...',
            ],
            global_variables=[],
        ),
        c_writer=Writer()
    )

    c_writer = map_result.c_writer
    c_writer.write('#include "Bindings.hpp"')

    for pytype in PyType.ALL_TYPES.values():
        if pytype.category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
            if pytype.name == 'ClassDB':
                # TODO: implement ClassDB singleton
                continue
            s1 = re.sub('(.)([A-Z][a-z0-9]+)', r'\1_\2', pytype.name)
            header_name = re.sub('([a-z])([A-Z])', r'\1_\2', s1).lower()
            c_writer.write(f'#include <godot_cpp/classes/{header_name}.hpp>')

    c_writer.write('')
    c_writer.write('namespace pkpy {')
    c_writer.write('')
    c_writer.write('void setup_bindings_generated() {')
    c_writer.indent()
    
    # ===============================
    # MARK: class single
    # ===============================
    class_single_classes: list[PyClass] = []
    for cls_data in gdt_all_in_one.classes:
        descriptions: list[str] = []
        if cls_data.brief_description:
            descriptions.append(cls_data.brief_description)
        if cls_data.description:
            descriptions.append(cls_data.description)
        if descriptions:
            description = '"""' + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
        pyclass = PyClass(
            type=PyType.get(cls_data.name),
            description_lines = descriptions,
            members = [],
            class_attributes = [],
            methods = [],
        )
        # 处理各种属性
        _map_class_properties(cls_data.properties, pyclass)
        _map_methods(cls_data, pyclass)
        _map_class_constants(cls_data.constants, pyclass)
        _map_signals(cls_data, pyclass)
        class_single_classes.append(pyclass)

    # ===============================
    # MARK: builtin class
    # ===============================
    builtin_classes: list[PyClass] = []
    for cls_data in gdt_all_in_one.builtin_classes:
        descriptions: list[str] = []
        if cls_data.brief_description:
            descriptions.append(cls_data.brief_description)
        if cls_data.description:
            descriptions.append(cls_data.description)
        if descriptions:
            description = '"""' + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
        pyclass = PyClass(
            type=PyType.get(cls_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
        # 处理各种属性
        _map_methods(cls_data, pyclass)
        _map_builtin_constants(cls_data.constants, pyclass)
        _map_operators(cls_data, pyclass)
        builtin_classes.append(pyclass)
    
    
    
    # ===============================
    # MARK: enum
    # ===============================
    # --- global enum ---
    enum_classes = []
    for enum_data in gdt_all_in_one.global_enums:
        descriptions: list[str] = []
        if enum_data.description:
            descriptions.append(enum_data.description)
        if descriptions:
            description = '"""' + "\n" + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
        
        pyclass = PyClass(
            type=PyType.get(enum_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        _map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)
    
    map_result.enum_pyi.classes.extend(enum_classes)
    
    # --- classes enum ---
    folded_enums = [(cls_data.name, cls_data.enums) for cls_data in gdt_all_in_one.classes]
    flattened_enums = [(cls_name, enum_data) for cls_name, enums in folded_enums for enum_data in enums or []]
    
    enum_classes: list[PyClass] = []
    for cls_name, enum_data in flattened_enums:
        descriptions: list[str] = []
        if enum_data.description:
            descriptions.append(enum_data.description)
        if descriptions:
            description = '"""' + "\n" + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()
            
        pyclass = PyClass(
            type=PyType.get(cls_name + '__' + enum_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        # 处理各种属性
        _map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)
    
    map_result.enum_pyi.classes.extend(enum_classes)
    
    
    # --- builtin class enum ---
    folded_enums = [(cls_data.name, cls_data.enums) for cls_data in gdt_all_in_one.builtin_classes]
    flattened_enums = [(cls_name, enum_data) for cls_name, enums in folded_enums for enum_data in enums or []]
    enum_classes = []
    for cls_name, enum_data in flattened_enums:
        descriptions: list[str] = []
        if enum_data.description:
            descriptions.append(enum_data.description)
        if descriptions:
            description = '"""' + "\n" + "\n".join(descriptions) + "\n" + '"""'
            descriptions = description.splitlines()

        pyclass = PyClass(
            type=PyType.get(cls_name + '__' + enum_data.name),
            description_lines=descriptions,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        _map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)
    
    map_result.enum_pyi.classes.extend(enum_classes)
    
    # ===============================
    # __init__.pyi
    # ===============================
    #
    #   Resource = GDNativeClass[_typings.Resource]('Resource')
    #   Engine = GDNativeSingleton[_typings.Engine]('Engine')
    for pytype in PyType.ALL_TYPES.values():
        if pytype.category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
            map_result.init_pyi.global_variables.append(SpecifiedPyMember(
                specified_string=f'{pytype.name} = GDNativeSingleton[_typings.{pytype.name}](\'{pytype.name}\')',
            ))
            if pytype.name == 'ClassDB':
                # TODO: implement ClassDB singleton
                continue
            c_writer.write(f'register_GDNativeSingleton("{pytype.name}", {pytype.name}::get_singleton());')

    c_writer.write('')
    for pytype in PyType.ALL_TYPES.values():
        if pytype.category == PyTypeCategory.GODOT_NATIVE:
            map_result.init_pyi.global_variables.append(SpecifiedPyMember(
                specified_string=f'{pytype.name} = GDNativeClass[_typings.{pytype.name}](\'{pytype.name}\')',
            ))
            c_writer.write(f'register_GDNativeClass("{pytype.name}");')
    
    # ===============================
    # enum.pyi
    # ===============================
    for enum_class in enum_classes:
        map_result.enum_pyi.classes.append(enum_class)
    
    # ===============================
    # typings.pyi
    # ===============================
    for class_single_class in class_single_classes:
        map_result.typings_pyi.classes.append(class_single_class)
    
    for builtin_class in builtin_classes:
        map_result.typings_pyi.classes.append(builtin_class)
    
    #   Variant
    pyclass = PyClass(
        type=PyType.get('Variant'),
        description_lines=[],
        members=[],
        class_attributes=[],
        methods=[],
    )
    map_result.typings_pyi.classes.append(pyclass)
    
    #   intptr
    map_result.typings_pyi.global_variables.append(SpecifiedPyMember(
        specified_string='intptr = int',
        inline_comment='intptr is a pointer to an unknown type (const void*)',
    ))

    c_writer.dedent()
    c_writer.write('}')
    c_writer.write('')
    c_writer.write('} // namespace pkpy')
    
    return map_result