from unittest import signals
from .schema_gdt import *

from . import enum
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


def fill_converters(gdt_all_in_one: GodotInOne):  
    '''
    使用gdt_all_in_one的信息初始化converters模块下的全局变量
    '''
    converters.BUILTIN_TYPES.update(
        set(cls.name for cls in gdt_all_in_one.builtin_classes)
    )
    
    converters.NATIVE_TYPES.update(set(cls.name for cls in gdt_all_in_one.classes))
    
    for cls_data in gdt_all_in_one.classes + gdt_all_in_one.builtin_classes:
        if not cls_data.enums:
            continue
        cls_name = cls_data.name
        enum_cls_name = f"{cls_name}StaticExtension"
    
        for enum_data in cls_data.enums:
            for v in enum_data.values or []:
                # HTTPRequest, HTTPRequest.Result, HTTPRequestStaticExtension, Result, RESULT_SUCCESS, 0
                # HTTPRequest, HTTPRequest.Result, HTTPRequestStaticExtension, Result, RESULT_CHUNKED_BODY_SIZE_MISMATCH, 1
                # HTTPRequest, HTTPRequest.Result, HTTPRequestStaticExtension, Result, ..., ...
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
    
    

def gen_c_writer(gdt_all_in_one:GodotInOne, c_writer: Writer) -> Writer:
    c_writer.write(
"""\
#include "Bindings.hpp"
"""
    )
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

    for clazz in gdt_all_in_one.singletons:
        cpp_name = clazz.name
        if cpp_name == "ClassDB":
            cpp_name = "ClassDBSingleton"
        c_writer.write(
            f'register_GDNativeSingleton("{clazz.name}", {cpp_name}::get_singleton());'
        )

    for clazz in gdt_all_in_one.builtin_classes + gdt_all_in_one.classes:
        variant_type = converters.CLASS_TO_VARIANT_TYPE.get(clazz.name, 'Variant::OBJECT')
        c_writer.write(f'register_GDNativeClass({variant_type}, "{clazz.name}");')
    for enum in gdt_all_in_one.global_enums:
        for v in enum.values:
            c_writer.write(f'register_GlobalConstant("{v.name}", {v.value});')
    
    c_writer.dedent()
    c_writer.write("}")
    c_writer.write("")
    c_writer.write("} // namespace pkpy")
    
    return c_writer

def gen_typings_pyi_writer(gdt_all_in_one: GodotInOne, pyi_writer: Writer) -> Writer:
    pyi_writer.write(
"""\
import typing
from typing import overload
from .enums import *
from . import alias


intptr = int

def default(gdt_expr: str) -> typing.Any: ...

"""
    )
    class_writer: Writer = pyi_writer
    
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
                    right_type_is_alias = right_type in list(converters.ALIAS_CLASS_DATA.loc[:, "cls_name"])
    
                    if converters.is_overload_operator(class_name, operator_name):
                        class_writer.write("@overload")
    
                    if right_type:
                        alias_module_path = "alias"
                        if right_type_is_alias:
                            class_writer.write(
                                f"def {operator_name}(self, right_{right_type}: {alias_module_path}.{right_type}) -> {return_type}: ..."
                            )
                        else:
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
                    arg_type_is_alias = arg_type in list(converters.ALIAS_CLASS_DATA.loc[:, "cls_name"])
                    
                    if arg.default_value:
                        arg_default_value = f"default({arg.default_value!r})"
                    else:
                        arg_default_value = None
    
                    if arg_type_is_alias:
                        alias_module_path = "alias"
                        expr = f"{arg_name}: {alias_module_path}.{arg_type}"
                    else:
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
    
    
    return pyi_writer

def gen_alias_pyi_writer(gdt_all_in_one: GodotInOne, pyi_writer: Writer) -> Writer:
    
    modules = map(str, set(converters.ALIAS_CLASS_DATA.loc[:, "module_abs_path"]))
    
    pyi_writer.write(
f'''\
import {', '.join(modules)}
from . import classes


'''
    )
    
    # 只有builtin_classes才有替用的类
    for clazz in gdt_all_in_one.builtin_classes:
        cls_name = converters.convert_class_name(clazz.name)
        found_records = converters.find_records(converters.ALIAS_CLASS_DATA, {"cls_name":cls_name})
        if len(found_records) > 0:
            
            alternative_cls_with_module_exprs: list[str] = []  # ["vmath.vec2", "vmath.vec3", ...]
            for _, record in found_records.iterrows():
                alternative_cls_with_module_exprs.append(record.loc['module_abs_path'] + "." + record.loc['alternative_cls_name'])
                
            pyi_writer.writefmt("{0} = classes.{1} | {2}",
                cls_name,
                cls_name,
                " | ".join(alternative_cls_with_module_exprs)
            )
        
    
    return pyi_writer


def gen_init_pyi_writer(gdt_all_in_one: GodotInOne, pyi_writer: Writer) -> Writer:
    pyi_writer.write(
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
    )
    
    init_writer = pyi_writer
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
    
    
    return pyi_writer


def gen_enums_pyi_writer(gdt_all_in_one: GodotInOne, pyi_writer: Writer) -> Writer:
    pyi_writer.write(
"""\
from typing import Literal
"""
    )
    # --- global enum ---
    enum.gen_global_enums(pyi_writer, gdt_all_in_one.global_enums)
    
    # --- classes enum ---
    enums_w = pyi_writer
    
    for cls_data in gdt_all_in_one.classes + gdt_all_in_one.builtin_classes:
        if not cls_data.enums:
            continue
        cls_name = cls_data.name
        enum_cls_name = f"{cls_name}StaticExtension"
        enums_w.write(f"class {enum_cls_name}:")
        enums_w.indent()
    
        for enum_data in cls_data.enums:
    
            if isinstance(enum_data, ClassesStaticExtension):
                enum.gen_class_enum(enums_w, enum_data)
            else:
                enum.gen_builtin_class_enum(enums_w, enum_data)
    
        enums_w.dedent()
        enums_w.write("\n")
    
    return pyi_writer



def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> MapResult:
    
    map_result = MapResult(
        typings_pyi= Writer(),
        init_pyi= Writer(),
        alias_pyi= Writer(),
        enums_pyi= Writer(),
        c_writer= Writer(), 
    )

    gen_c_writer(gdt_all_in_one, map_result.c_writer)  # 暂不依赖converters
    
    fill_converters(gdt_all_in_one)
    gen_alias_pyi_writer(gdt_all_in_one, map_result.alias_pyi)
    gen_enums_pyi_writer(gdt_all_in_one, map_result.enums_pyi)
    gen_init_pyi_writer(gdt_all_in_one, map_result.init_pyi)
    gen_typings_pyi_writer(gdt_all_in_one, map_result.typings_pyi)
    
    return map_result
