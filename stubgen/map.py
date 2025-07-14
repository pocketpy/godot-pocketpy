from unittest import signals
from .schema_gdt import *

from .enum import gen_global_enums, gen_class_enum, gen_builtin_class_enum
from .writer import Writer

import re
from . import converters

# ===============================
# 入口
# ===============================


@dataclass
class MapResult:
    typings_pyi: Writer
    enums_pyi: Writer
    init_pyi: Writer
    alias_pyi: Writer
    c_writer: Writer


def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> MapResult:

    # ================
    # 文件头
    # ================
    map_result = MapResult(
        typings_pyi=Writer().write(
"""\
import typing
from typing import overload
from .enums import *


intptr = int

def default(gdt_expr: str) -> typing.Any: ...

"""
        ),
        enums_pyi=Writer().write("from typing import Literal\n\n"),
        init_pyi=Writer().write(
"""\
from . import classes
from . import enums

class PythonScriptInstance[T: classes.Object]:
    @property
    def owner(self) -> T: ...

class GDNativeClass[T: classes.Object]:
    @property
    def script(self) -> PythonScriptInstance[T]: ...
    def __new__(cls) -> T: ...

class GDBuiltinClass[T: classes.Variant]: ...


"""
        ),
        alias_pyi=Writer().write(
'''\
import vmath
'''
        ),
        c_writer=Writer(),
    )

    c_writer = map_result.c_writer
    c_writer.write('#include "Bindings.hpp"')

    # for pytype in PyType.ALL_TYPES.values():
    #     if pytype.category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
    #         if pytype.name == "ClassDB":
    #             header_name = 'class_db_singleton'
    #         else:
    #             s1 = re.sub("(.)([A-Z][a-z0-9]+)", r"\1_\2", pytype.name)
    #             header_name = re.sub("([a-z])([A-Z])", r"\1_\2", s1).lower()
    #         c_writer.write(f"#include <godot_cpp/classes/{header_name}.hpp>")

    for clazz in gdt_all_in_one.singletons:
        if clazz.name == "ClassDB":
            header_name = "class_db_singleton"
        else:
            s1 = re.sub("(.)([A-Z][a-z0-9]+)", r"\1_\2", clazz.name)
            header_name = re.sub("([a-z])([A-Z])", r"\1_\2", s1).lower()
        c_writer.write(f"#include <godot_cpp/classes/{header_name}.hpp>")

    c_writer.write("")
    c_writer.write("namespace pkpy {")
    c_writer.write("")
    c_writer.write("void setup_bindings_generated() {")
    c_writer.indent()

    # ===============================
    # MARK: build converters
    # ===============================
    converters.BUILTIN_TYPES.update(
        set(cls.name for cls in gdt_all_in_one.builtin_classes)
    )

    converters.NATIVE_TYPES.update(set(cls.name for cls in gdt_all_in_one.classes))

    for cls_data in gdt_all_in_one.classes + gdt_all_in_one.builtin_classes:
        if not cls_data.enums:
            continue
        cls_name = cls_data.name
        enum_cls_name = f"{cls_name}Enum"

        for enum_data in cls_data.enums:
            for v in enum_data.values or []:
                # HTTPRequest, HTTPRequest.Result, HTTPRequestEnum, Result, RESULT_SUCCESS, 0
                # HTTPRequest, HTTPRequest.Result, HTTPRequestEnum, Result, RESULT_CHUNKED_BODY_SIZE_MISMATCH, 1
                # HTTPRequest, HTTPRequest.Result, HTTPRequestEnum, Result, ..., ...
                converters.append_records(
                    converters.CLASS_ENUM_DATA,
                    {
                        "cls_name": cls_name,
                        "orign_enum_name": cls_name + "." + enum_data.name,
                        "cls_enum_name": enum_cls_name,
                        "enum_name": enum_data.name,
                        "enum_constant_name": v.name,
                        "constant_value": v.value,
                    },
                )

    for enum in gdt_all_in_one.global_enums:
        if "." in enum.name:
            cls_name, enum_name = enum.name.split(".")
            for v in enum.values:
                # Variant.Type, Variant_Type, TYPE_NIL, 0
                # Variant.Type, Variant_Type, TYPE_BOOL, 1
                # Variant.Type, Variant_Type, ..., ...
                converters.append_records(
                    converters.GLOBAL_ENUMS_DATA,
                    {
                        "orign_enum_name": enum.name,
                        "converted_enum_name": cls_name + "_" + enum_name,
                        "enum_constant_name": v.name,
                        "constant_value": v.value,
                    },
                )

        else:
            for v in enum.values:
                # MethodFlags, MethodFlags, METHOD_FLAG_NORMAL, 1
                # MethodFlags, MethodFlags, METHOD_FLAG_EDITOR, 2
                # MethodFlags, MethodFlags, ..., ...
                converters.append_records(
                    converters.GLOBAL_ENUMS_DATA,
                    {
                        "orign_enum_name": enum.name,
                        "converted_enum_name": enum.name,
                        "enum_constant_name": v.name,
                        "constant_value": v.value,
                    },
                )

    for builtin_class in gdt_all_in_one.builtin_classes:
        cls_name = converters.convert_class_name(builtin_class.name)
        if builtin_class.operators:
            for op in builtin_class.operators:
                if converters.is_supported_operator(op.name):
                    op_name = converters.convert_operator_to_method_name(op.name)
                    converters.append_records(
                        converters.BUILTIN_CLASSES_SUPPORTED_OPERATOR_DATA,
                        {
                            "orign_cls_name": builtin_class.name,  # 原始的类名
                            "cls_name": cls_name,  # 转换后的类名
                            "orign_op_name": op.name,  # 原始的运算符名称
                            "op_name": op_name,  # 转换后的运算符名称
                        },
                    )


    # ===============================
    # MARK: enum
    # ===============================
    # --- global enum ---
    gen_global_enums(map_result.enums_pyi, gdt_all_in_one.global_enums)

    # --- classes enum ---
    enums_w = map_result.enums_pyi

    for cls_data in gdt_all_in_one.classes + gdt_all_in_one.builtin_classes:
        if not cls_data.enums:
            continue
        cls_name = cls_data.name
        enum_cls_name = f"{cls_name}Enum"
        enums_w.write(f"class {enum_cls_name}:")
        enums_w.indent()

        for enum_data in cls_data.enums:

            if isinstance(enum_data, ClassesEnum):
                gen_class_enum(enums_w, enum_data)
            else:
                gen_builtin_class_enum(enums_w, enum_data)

        enums_w.dedent()
        enums_w.write("\n")

    # ===============================
    # __init__.pyi
    # ===============================
    #
    #   Resource = GDNativeClass[_typings.Resource]('Resource')
    #   Engine = GDNativeSingleton[_typings.Engine]('Engine')
    # for pytype in PyType.ALL_TYPES.values():
    #     if pytype.category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
    #         map_result.init_pyi.write(f"{pytype.name}: _typings.{pytype.name}")

    #         cpp_name = pytype.name
    #         if cpp_name == "ClassDB":
    #             cpp_name = "ClassDBSingleton"
    #         c_writer.write(
    #             f'register_GDNativeSingleton("{pytype.name}", {cpp_name}::get_singleton());'
    #         )

    # c_writer.write("")
    # for pytype in PyType.ALL_TYPES.values():
    #     if pytype.category == PyTypeCategory.GODOT_NATIVE:
    #         if pytype.name in PyType.NO_OBJECT_VARIANT_TYPES:
    #             map_result.init_pyi.write(f"{pytype.name}: GDBuiltinClass[_typings.{pytype.name}]")
    #         else:
    #             map_result.init_pyi.write(f"{pytype.name}: GDNativeClass[_typings.{pytype.name}]")
    #         c_writer.write(f'register_GDNativeClass("{pytype.name}");')



    # ======MARK: Builtin + Native
    class_writer: Writer = map_result.typings_pyi

    # -----手动定义Variant
    class_writer.write("class Variant:")
    class_writer.indent()
    class_writer.write("...")
    class_writer.dedent()
    class_writer.write("")

    for clazz in gdt_all_in_one.builtin_classes + gdt_all_in_one.classes:

        is_empty_class: bool = True
        # ------class xxx(xxx):
        class_name: str = converters.convert_class_name(clazz.name)

        if isinstance(clazz, BuiltinClass):
            class_inherits = "Variant"
        else:
            class_inherits = (
                converters.convert_class_name(clazz.inherits)
                if clazz.inherits
                else None
            )

        class_writer.writefmt(
            "class {0}{1}:", class_name, f"({class_inherits})" if class_inherits else ""
        )

        class_writer.indent()

        # ------Member variables
        if isinstance(clazz, BuiltinClass):
            member_vars = clazz.members
        else:
            member_vars = clazz.properties

        if member_vars:
            for member_data in member_vars:

                member_name: str = converters.convert_keyword_name(member_data.name)
                member_type: str = converters.convert_type_name(member_data.type)

                class_writer.writefmt("{0}: {1}", member_name, member_type)

            class_writer.write("")
            is_empty_class = False

        # ------Signals
        if isinstance(clazz, BuiltinClass):
            signals = None
        else:
            signals = clazz.signals

            if signals:

                for signal in signals:
                    signal_name = converters.convert_keyword_name(signal.name)
                    signal_args = signal.arguments or []

                    arg_comment_expr_list = []
                    arg_expr_list = []
                    for signal_arg in signal_args:

                        arg_name = converters.convert_keyword_name(signal_arg.name)
                        arg_type = converters.convert_type_name(signal_arg.type)

                        arg_comment_expr_list.append(arg_name + ":" + arg_type)
                        arg_expr_list.append(arg_type)

                    class_writer.writefmt(
                        "{0}: Signal[typing.Callable[[{1}], None]]  # {2}",
                        signal.name,
                        ", ".join(arg_expr_list),
                        (
                            ", ".join(arg_comment_expr_list)
                            if arg_comment_expr_list
                            else "no arguments"
                        ),
                    )

                class_writer.write("")
                is_empty_class = False
                
        # ------Class variables
        if isinstance(clazz, BuiltinClass):
            class_consts = clazz.constants
        else:
            class_consts = clazz.constants

        if class_consts:
            for const in class_consts:
                const_name = converters.convert_keyword_name(const.name)
                value = str(const.value)
                class_writer.write(f"{const_name} = default({value!r})")  # TODO

            class_writer.write("")
            is_empty_class = False

        # ------Operators
        if isinstance(clazz, BuiltinClass):
            operators = clazz.operators
        else:
            operators = None

        if operators:
            for operator in operators:
                orign_operator_name = operator.name

                if converters.is_supported_operator(orign_operator_name):
                    operator_name = converters.convert_operator_to_method_name(
                        orign_operator_name
                    )
                    return_type = operator.return_type
                    right_type = operator.right_type

                    if converters.is_overload_operator(class_name, operator_name):
                        class_writer.write("@overload")

                    if right_type:
                        class_writer.write(
                            f"def {operator_name}(self, right_{right_type}: {right_type}) -> {return_type}: ..."
                        )
                    else:
                        class_writer.write(
                            f"def {operator_name}(self) -> {return_type}: ..."
                        )
                        
            class_writer.write("")
            is_empty_class = False

        # ------Class methods
        if clazz.methods:
            for method in clazz.methods:
                ret_t = "None"
                if isinstance(method, (ClassesMethod, ClassesMethodVirtual)):
                    if method.return_value:
                        ret_t = converters.convert_type_name(method.return_value.type)
                else:
                    ret_t = (
                        converters.convert_type_name(method.return_type)
                        if method.return_type
                        else "None"
                    )

                # ------Arguments
                arg_expr = []
                if method.is_static:
                    class_writer.write("@staticmethod")
                else:
                    arg_expr.append("self")

                for arg in method.arguments or []:

                    arg_name = converters.convert_keyword_name(arg.name)
                    arg_type = converters.convert_type_name(arg.type)
                    if arg.default_value:
                        arg_default_value = f"default({arg.default_value!r})"
                    else:
                        arg_default_value = None

                    expr = f"{arg_name}: {arg_type}"
                    if arg.default_value is not None:
                        expr += f" = {arg_default_value}"
                    arg_expr.append(expr)

                if method.is_vararg:
                    arg_expr.append(f"*args")

                # ------Method
                method_name = converters.convert_keyword_name(method.name)
                class_writer.writefmt(
                    "def {0}({1}) -> {2}: ...",
                    method_name,
                    ", ".join(arg_expr),
                    ret_t,
                )

            class_writer.write("")
            is_empty_class = False

        if is_empty_class:
            class_writer.write("...")
        class_writer.dedent()
        class_writer.write("")


    # ======MARK: __init__.pyi
    init_writer = map_result.init_pyi
    for clazz in gdt_all_in_one.builtin_classes + gdt_all_in_one.classes:
        cls_name = converters.convert_class_name(clazz.name)
        cls_type_name = converters.convert_class_name(clazz.name).split('[')[0]  # 忽略模板参数
        records = converters.find_records(converters.CLASS_ENUM_DATA, {'cls_name': cls_name})
        cls_enum = None
        if len(records) > 0:
            cls_enum = records.iloc[0].loc['cls_enum_name']
        
        if isinstance(clazz, BuiltinClass):
            inherit_1 = f'GDBuiltinClass[classes.{cls_type_name}]'
        else:
            inherit_1 = f'GDNativeClass[classes.{cls_type_name}]'
        
        if cls_enum:
            inherit_2 = f'enums.{cls_enum}'
        else:
            inherit_2 = None
        
        if inherit_2:
            init_writer.write(f'class {cls_name}({inherit_1}, {inherit_2}): ...')
        else:
            init_writer.write(f'class {cls_name}({inherit_1}): ...')
    
    
    # ======MARK: alias.pyi
    alias_writer = map_result.alias_pyi
    


    # # 折叠

    # # =======Builtin Classes=======
    # builtin_class_writer: Writer = map_result.typings_pyi
    # for builtin_class_data in gdt_all_in_one.builtin_classes:

    #     # ------class xxx(xxx):
    #     class_name: str = builtin_class_data.name
    #     class_inherits: str|None = "Variant"

    #     builtin_class_writer.write(
    #         "class {0}{1}:".format(
    #             class_name,
    #             f"({class_inherits})" if class_inherits else ""
    #         )
    #     )

    #     builtin_class_writer.indent()
    #     # ------Member variables

    #     builtin_class_member_vars: list[BuiltinClassMember]|None = builtin_class_data.members

    #     if builtin_class_member_vars:
    #         for member_data in builtin_class_member_vars:

    #             member_name: str = member_data.name
    #             member_type: str = "Any"
    #             member_desc: str|None = member_data.description

    #             builtin_class_writer.write(
    #                 f'{member_name}: {member_type}' + f"# {member_desc}" if member_desc else ""
    #                 )

    #         builtin_class_writer.write('')
    #     # ------Class variables

    #     class_vars: list[BuiltinClassConstant]|None = builtin_class_data.constants

    #     if class_vars:
    #         for class_var_data in class_vars:

    #             class_var_name: str = class_var_data.name
    #             class_var_value: int = "default"
    #             class_var_desc: str|None = class_var_data.description

    #             if class_var_desc:
    #                 builtin_class_writer.write(f"{class_var_name} = {class_var_value}  # {class_var_desc}")
    #             else:
    #                 builtin_class_writer.write(f'{class_var_name} = {class_var_value}')

    #         builtin_class_writer.write('')
    #     # ------Operators
    #     operators: list[BuiltinClassOperator]|None = builtin_class_data.operators

    #     if operators:
    #         for operator in operators:

    #             # TODO: 筛选和转换

    #             operator_name = operator.name
    #             operator_right_type: str = "Any"
    #             operator_return_type: str = "Any"

    #             builtin_class_writer.write(
    #                 f'def {operator_name}(self, {operator_right_type} -> {operator_return_type}:'
    #             )

    #             builtin_class_writer.indent()
    #             builtin_class_writer.write("...")
    #             builtin_class_writer.dedent()

    #     # ------'__init__'s
    #     constructers: list[BuiltinClassConstructor]|None = builtin_class_data.constructors
    #     if constructers:
    #         for constructer in constructers:

    #             # ------__init__ parameters
    #             constructer_params: list[BuiltinClassConstructorArgument]|None = constructer.arguments

    #             params: list[str] = []
    #             if constructer_params:
    #                 for arg in constructer_params:

    #                     arg_name: str = arg.name
    #                     arg_type: str = arg.type

    #                     params.append(f'{arg_name}: {arg_type}')

    #             # ------__init__
    #             params_str: str = ", ".join(params)
    #             is_overload: bool = len(constructers) > 1

    #             if is_overload:
    #                 builtin_class_writer.write('@overload')

    #             builtin_class_writer.write((f'def __init__(self, {params_str}):'))

    #             builtin_class_writer.indent()
    #             builtin_class_writer.dedent()

    #     # ------Class methods

    #     class_methods: list[BuiltinClassMethod]|None = builtin_class_data.methods

    #     if class_methods:
    #         for method_data in class_methods:

    #             # ------Method parameters
    #             method_params: list[BuiltinClassMehodArgument]|None = method_data.arguments

    #             params: list[str] = []
    #             if method_params:
    #                 for arg in method_params:

    #                     arg_name: str = arg.name
    #                     arg_type: str = arg.type
    #                     arg_default_value: str|None = arg.default_value

    #                     if arg_default_value:
    #                         params.append(f'{arg_name}: {arg_type} = {arg_default_value}')
    #                     else:
    #                         params.append(f'{arg_name}: {arg_type}')

    #             # ------Method
    #             params_str: str = ", ".join(params)
    #             method_name: str = method_data.name
    #             method_return_type: str|None = method_data.return_type
    #             is_static: bool = method_data.is_static
    #             is_abstract: bool = method_data.is_vararg
    #             is_const: bool = method_data.is_const  #  ???

    #             if is_static:
    #                 builtin_class_writer.write("@staticmethod")
    #             if method_return_type:
    #                 builtin_class_writer.write(f'def {method_name}({params_str}) -> {method_return_type}:')
    #             else:
    #                 builtin_class_writer.write(f'def {method_name}({params_str}):')

    #             builtin_class_writer.indent()
    #             builtin_class_writer.write('...')
    #             builtin_class_writer.dedent()

    #         builtin_class_writer.write("")

    #     builtin_class_writer.dedent()

    # # =======Native Classe======
    # native_class_writer: Writer = map_result.typings_pyi
    # for native_class_data in gdt_all_in_one.classes:

    #     # ------class xxx(xxx):
    #     class_name: str = native_class_data.name
    #     class_inherits: str|None = "Any"

    #     native_class_writer.write(
    #         "class {0}{1}:".format(
    #             class_name,
    #             f"({class_inherits})" if class_inherits else ""
    #         )
    #     )

    #     native_class_writer.indent()
    #     # ------Member variables

    #     native_class_member_vars: list[ClassesProperty]|None = native_class_data.properties

    #     if native_class_member_vars:
    #         for member_data in native_class_member_vars:

    #             member_name: str = member_data.name
    #             member_type: str = member_data.type
    #             member_desc: str|None = member_data.description

    #             builtin_class_writer.write(
    #                 f'{member_name}: {member_type}' + f"# {member_desc}" if member_desc else ""
    #                 )

    #         builtin_class_writer.write('')

    #     # ------Signals

    #     class_signals: list[ClassesSignal]|None = native_class_data.signals

    #     if class_signals:
    #         for signal in class_signals:

    #             # ------Signal params
    #             signal_params: list[ClassesSignalArgument]|None = signal.arguments

    #             param_types: list[str] = []
    #             param_names: list[str] = []
    #             if signal_params:
    #                 for arg in signal_params:

    #                     arg_name: str = arg.name
    #                     arg_type: str = arg.type

    #                     param_types.append(f'{arg_type}')
    #                     param_names.append(f'{arg_name}')

    #             # ------Signal
    #             params_str: str = ', '.join(param_types)
    #             params_comment_str: str = ', '.join([f'{name}: type' for name, type in zip(param_names, param_types)])
    #             signal_name: str = signal.name
    #             signal_desc: str|None = signal.description

    #             if signal_desc:
    #                 native_class_writer.write(f'{signal_name} = Signal[typing.Callable[{params_str}, None]]:  # {signal_desc} {params_comment_str}')
    #             else:
    #                 native_class_writer.write(f'{signal_name} = Signal[typing.Callable[{params_str}, None]]:    # {params_comment_str}')

    #     # ------Class variables
    #     class_vars: list[ClassesConstant]|None = native_class_data.constants

    #     if class_vars:
    #         for class_var_data in class_vars:

    #             class_var_name: str = class_var_data.name
    #             class_var_value: int = class_var_data.value
    #             class_var_desc: str|None = class_var_data.description

    #             if class_var_desc:
    #                 builtin_class_writer.write(f"{class_var_name} = {class_var_value}  # {class_var_desc}")
    #             else:
    #                 builtin_class_writer.write(f'{class_var_name} = {class_var_value}')

    #         builtin_class_writer.write('')
    #     # ------Properties
    #     class_properties: list[ClassesProperty]|None = native_class_data.properties

    #     if class_properties:
    #         for class_property in class_properties:

    #             class_property_type: str = class_property.type
    #             class_property_name: str = class_property.name
    #             class_property_desc: str|None = class_property.description

    #             native_class_writer.write('@property')
    #             if class_property_desc:
    #                 native_class_writer.write(
    #                     f"def {class_property_name}(self) -> {class_property_type}:"
    #                 )

    #             native_class_writer.indent()

    #             if class_property_desc:

    #                 native_class_writer.write(f'"""{class_property_desc}"""')
    #             native_class_writer.write('...')
    #             native_class_writer.dedent()

    #     # ------Methods

    #         # ------Static methods

    #         # ------Instance methods

    #     native_class_writer.dedent()

    # --------C----------
    c_writer.dedent()
    c_writer.write("}")
    c_writer.write("")
    c_writer.write("} // namespace pkpy")

    return map_result
