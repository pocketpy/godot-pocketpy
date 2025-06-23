from attr import dataclass
from .schema import load_extension_api, ClassesSingle, BuiltinClass, GlobalEnum
from keyword import iskeyword
from .config import *

BUILTIN_TYPES = {
    'None', 'int', 'float', 'bool', 'str'
}

# https://github.com/pocketpy/godot-pocketpy/blob/main/src/lang/Common.cpp#L194
# 	DEF_BINARY_OP("__eq__", OP_EQUAL)
# 	DEF_BINARY_OP("__ne__", OP_NOT_EQUAL)
# 	DEF_BINARY_OP("__lt__", OP_LESS)
# 	DEF_BINARY_OP("__le__", OP_LESS_EQUAL)
# 	DEF_BINARY_OP("__gt__", OP_GREATER)
# 	DEF_BINARY_OP("__ge__", OP_GREATER_EQUAL)
# 	DEF_BINARY_OP("__add__", OP_ADD)
# 	DEF_BINARY_OP("__sub__", OP_SUBTRACT)
# 	DEF_BINARY_OP("__mul__", OP_MULTIPLY)
# 	DEF_BINARY_OP("__truediv__", OP_DIVIDE)
# 	DEF_BINARY_OP("__mod__", OP_MODULE)
# 	DEF_BINARY_OP("__pow__", OP_POWER)
# 	DEF_BINARY_OP("__lshift__", OP_SHIFT_LEFT)
# 	DEF_BINARY_OP("__rshift__", OP_SHIFT_RIGHT)
# 	DEF_BINARY_OP("__and__", OP_BIT_AND)
# 	DEF_BINARY_OP("__or__", OP_BIT_OR)
# 	DEF_BINARY_OP("__xor__", OP_BIT_XOR)
# 	DEF_BINARY_OP("__contains__", OP_IN)
# 	DEF_UNARY_OP("__neg__", OP_NEGATE)
# 	DEF_UNARY_OP("__invert__", OP_BIT_NEGATE)

# Binary operators
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


class Writer:
    def __init__(self) -> None:
        self.buffer = []
        self.indent_level = 0

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level -= 1

    def write(self, line: str):
        self.buffer.append('    ' * self.indent_level + line)

    def __str__(self) -> str:
        return '\n'.join(self.buffer)


def wrap_builtin_type(t: str, need_quote: bool=True):
    if t in BUILTIN_TYPES:
        return t
    else:
        t = t.replace('enum::', '')
        t = t.replace('.', '_')
        t = t.replace('bitfield::', '')  # v2 bitfield::xxx -> xxx
        t = 'intptr' if "*" in t else t  # v2 intptr -> int
        t = t.replace('typedarray::', 'list[') + ']' if 'typedarray::' in t else t  # v2 typedarray::xxx -> list[xxx]
        t = t.split(',')[0] if "," in t else t  # v2 BaseResourceClass,ResourceClass -> BaseResource
        return f'\'{t}\'' if need_quote else f'{t}'


@dataclass
class WrapValueReturnValue:
    result: str|int|float|bool|None|list|dict
    add_None: bool = False
    

def _wrap_positioned_arg_list(arg_list_str: str, context = []) -> str:
    if arg_list_str == '':
        return ''
    args = arg_list_str.split(', ')
    wrapped_args = ', '.join([str(wrap_value(arg, [context, [i,arg]]).result) for i,arg in enumerate(args)])
    return wrapped_args

def wrap_value(t: str, context = []):
    
    # ===返回值===
    result = None
    add_None = False
    # ===========
    
    
    # 处理转义字符
    # escaped_t = t.replace('\\', '\\\\').replace('"', '\\"')
    
    
    
    # 使用单层条件判断处理所有情况
    
    # 基本类型处理
    is_int = False
    is_float = False
    try:
        int(t)
        is_int = True
    except Exception:
        try:
            float(t)
            is_float = True
        except Exception:
            pass
    if is_int:
        result = t
    elif is_float:
        result = t
    elif t == 'true':
        result = True
    elif t == 'false':
        result = False
    elif t == 'null':
        result = None
        add_None = True
    elif t == '\'inf\'':
        result = 'float("inf")'
    elif t == '\'-inf\'':
        result = 'float("-inf)'
    
    # 类实例化处理
    elif '(' in t and ')' in t:
        all_class_names = [c.name for c in (all_builtin_classes + all_classes)]
        class_name_with_generic = t.split('(')[0]
        # 解析泛型
        generic_class = None
        if '[' in class_name_with_generic:
            class_name, generic_class = class_name_with_generic.split('[')
            generic_class = generic_class.split(']')[0]
        else:
            class_name = class_name_with_generic
        # 泛型处理
        if generic_class:
            if generic_class in all_class_names:
                generic_class = f'{generic_class}[{generic_class}]'
            else:
                raise Exception(f'发现未知泛型类: {generic_class} (context: {context})')
        # 类实例化处理
        if class_name in all_class_names:
            wrapped_args = _wrap_positioned_arg_list(t.split('(')[-1].split(')')[0], context)
        else:
            raise Exception(f'发现未知类: {t} (context: {context})')
        
        generic_class_str = f"[{generic_class}]" if generic_class else ""
        result = f'{class_name}{generic_class_str}({wrapped_args})'
    
    # 字符串处理
    elif t.startswith('"') and t.endswith('"'):
        result = t
    elif t == '&""':  # &-string
        result = None
        add_None = True
    elif t.startswith('&"') and t.endswith('"'):
        
        if "{" in t and "}" in t:
            # f-string字面量
            result = 'f'+t[1:]
            print(f'Warning: 发现f-string字面量: {t} (context: {context})')
        else:
            # 降级为普通str
            result = t[1:]
        
        
        
    # 数组处理
    elif t == '[]':
        result = None
        add_None = True
    elif t.startswith('[') and t.endswith(']'):
        wrapped_args = _wrap_positioned_arg_list(t.split('[')[-1].split(']')[0], context)
        result = f'[{wrapped_args}]'
    # 字典处理
    elif t == '{}':
        result = None
        add_None = True
    elif t.startswith('{') and t.endswith('}'):
        raise Exception(f'发现非空字典字面量: {t} (context: {context})')
    
    # 善后
    else:
        raise Exception(f'发现未知值: {t} (context: {context})')
    
    return WrapValueReturnValue(result, add_None)

def wrap_value(t: str, _ = []):
    return WrapValueReturnValue(f'default(\'\'\'{t}\'\'\')', False)


def wrap_keyword(t: str):
    if iskeyword(t):
        return f'{t}_'
    return f'{t}'

def global_enum_to_pyi(global_enum: GlobalEnum, pyi_w: Writer) -> None:
    assert pyi_w.indent_level == 0
    pyi_w.write(f'class {wrap_builtin_type(global_enum.name, False)}:')
    pyi_w.indent()
    for e in global_enum.values:
        pyi_w.write(f'{e.name} = {e.value}')
    pyi_w.write('')
    pyi_w.dedent()

def common_class_to_pyi(
    pyi_w: Writer,
    name: str,
    inherits: str | None,
    brief_description: str | None,
    description: str | None,
    constants: list | None,
    enums: list | None,
    methods: list | None,
    properties: list | None = None,
    signals: list | None = None,
    operators: list | None = None,
    is_builtin_class: bool = False
) -> None:
    """
    Common function to process both BuiltinClass and ClassesSingle with explicit parameters
    """
    assert pyi_w.indent_level == 0
    
    has_properties = False
    has_constants = False
    has_signals = False
    has_methods = False
    has_operators = False
    
    # Class declaration
    if inherits is None:
        if is_builtin_class:
            pyi_w.write(f'class {name}(BuiltinBase):')
        else:
            pyi_w.write(f'class {name}(NativeBase):')
    else:
        pyi_w.write(f"class {name}({inherits}):")
    pyi_w.indent()
    
    # Class documentation
    doc_text = ''
    if brief_description:
        doc_text += brief_description
        doc_text += '\t\n'
    if description:
        doc_text += description
        doc_text += '\t\n'
    if doc_text:
        pyi_w.write(f'"""{doc_text}')
        pyi_w.write(f'"""')
    
    # Properties (ClassesSingle only)
    if not is_builtin_class and properties:
        has_properties = True
        for p in properties:
            pyi_w.write(f'{wrap_keyword(p.name)}: {wrap_builtin_type(p.type)}')
    
    # Constants
    if constants:
        has_constants = True
        for c in constants:
            # Handle different constant value types between BuiltinClass and ClassesSingle
            if is_builtin_class:
                # BuiltinClass constants have string values
                if isinstance(c.value, str):
                    c.value = c.value.replace('inf', "float('inf')")
                pyi_w.write(f'{wrap_keyword(c.name)} = {wrap_value(c.value, [c]).result}')
            else:
                # ClassesSingle constants have integer values
                pyi_w.write(f'{wrap_keyword(c.name)} = {c.value}')
        pyi_w.write('')
    
    # Signals (ClassesSingle only)
    if not is_builtin_class and signals:
        has_signals = True
        for s in signals:
            if s.arguments:
                args = ", ".join([f"'{arg.type}'" for arg in s.arguments])
                args_in_comment = ", ".join([f"{arg.name}: {wrap_builtin_type(arg.type)}" for arg in s.arguments])
                pyi_w.write(f'{wrap_keyword(s.name)}: Signal[Callable[[{args}], None]]  # {s.name}({args_in_comment})')
            else:
                pyi_w.write(f'{wrap_keyword(s.name)}: Signal[Callable[[], None]]  # {s.name}()')
    
    # Operators (BuiltinClass only)
    if is_builtin_class and operators:
        has_operators = True
        for o in operators:
            if o.name in NOT_SUPPORTED_OPERATORS:
                continue
            if o.name in OPERATORS_TABLE:
                if o.right_type:
                    pyi_w.write(f'def {OPERATORS_TABLE[o.name]}(self, other: {wrap_builtin_type(o.right_type)}) -> {wrap_builtin_type(o.return_type)}: ...')
                else:
                    pyi_w.write(f'def {OPERATORS_TABLE[o.name]}(self) -> {wrap_builtin_type(o.return_type)}: ...')
            else:
                raise Exception(f'发现新的运算符: {o.name}')
    
    # Methods
    if methods:
        has_methods = True
        for m in methods:
            static_flag = m.is_static
            vararg_flag = m.is_vararg
            # make argument str, xx: type=val
            arg_list = []
            arg_self_str = 'self'
            arg_varg_str = '*arg'
            if m.arguments:
                arg_self_str = 'self, '
                arg_varg_str = ', *arg'
                for arg in m.arguments:
                    arg_val = ''
                    add_None = False
                    if hasattr(arg, 'default_value') and arg.default_value:
                        default_value_dataclass = wrap_value(arg.default_value, [arg])
                        add_None = default_value_dataclass.add_None
                        default_value_str = f' = {default_value_dataclass.result}'
                    arg_val += f'{wrap_keyword(arg.name)}: {wrap_builtin_type(arg.type)}{"|None" if add_None else ""}'
                    if hasattr(arg, 'default_value') and arg.default_value:
                        arg_val += default_value_str
                    arg_list.append(arg_val)
            arg_str = ', '.join(arg_list)
            # add @staticmethod
            if static_flag == True:
                pyi_w.write(f'@staticmethod')
            # add 'self' for general methods
            else:
                arg_str = arg_self_str + arg_str
            # add *arg
            if vararg_flag == True:
                arg_str += arg_varg_str
            # special case
            if arg_str == 'self*arg':
                arg_str = 'self, *arg'
            
            # Handle return value
            return_val = 'None'
            if hasattr(m, 'return_value') and m.return_value and hasattr(m.return_value, 'type'):
                return_val = m.return_value.type
            elif hasattr(m, 'return_type') and m.return_type:
                return_val = m.return_type
                
            pyi_w.write(f'def {wrap_keyword(m.name)}({arg_str}) -> {wrap_builtin_type(return_val)}: ...')
            
            # Method documentation
            method_description = ''
            if m.description:
                method_description = m.description
                pyi_w.indent()
                pyi_w.write(f'"""{method_description}')
                pyi_w.write(f'"""')
                pyi_w.dedent()
    
    # Add 'pass' if class is empty
    if (has_methods or has_constants or has_properties or has_signals or has_operators) == False:
        pyi_w.write('pass')
    pyi_w.write('')
    pyi_w.dedent()

def builtin_class_to_pyi(builtin_class: BuiltinClass, pyi_w: Writer) -> None:
    """Entry function for BuiltinClass"""
    assert pyi_w.indent_level == 0
    
    # Special case for Variant
    inherits = builtin_class.inherits if hasattr(builtin_class, 'inherits') else None
    if builtin_class.name == "Variant":
        inherits = None
    
    common_class_to_pyi(
        pyi_w=pyi_w,
        name=builtin_class.name,
        inherits=inherits,
        brief_description=builtin_class.brief_description,
        description=builtin_class.description,
        constants=builtin_class.constants,
        enums=builtin_class.enums,
        methods=builtin_class.methods,
        operators=builtin_class.operators,
        is_builtin_class=True
    )

def single_class_to_pyi(single_class: ClassesSingle, pyi_w: Writer) -> None:
    """Entry function for ClassesSingle"""
    assert pyi_w.indent_level == 0
    
    common_class_to_pyi(
        pyi_w=pyi_w,
        name=single_class.name,
        inherits=single_class.inherits,
        brief_description=single_class.brief_description,
        description=single_class.description,
        constants=single_class.constants,
        enums=single_class.enums,
        methods=single_class.methods,
        properties=single_class.properties,
        signals=single_class.signals,
        is_builtin_class=False
    )
            
all_in_one = load_extension_api(EXTENSION_API_PATH)
all_global_enums = all_in_one.global_enums
all_builtin_classes = all_in_one.builtin_classes
all_classes = all_in_one.classes

# Move Object from natives to builtins, adapting structure

# Find and remove Object from all_classes, and add to all_builtin_classes
object_class = None
for i, cls in enumerate(all_classes):
    if cls.name == "Object":
        object_class = all_classes.pop(i)
        break
if object_class is not None:
    # Remove fields that are not present in BuiltinClass, if necessary
    # BuiltinClass does not have: properties, signals, etc.
    # We'll keep only the fields that BuiltinClass expects.
    object_builtin = type("BuiltinClass", (), {})()
    object_builtin.name = object_class.name
    object_builtin.inherits = 'NativeBase'
    object_builtin.brief_description = getattr(object_class, "brief_description", "")
    object_builtin.description = getattr(object_class, "description", "")
    object_builtin.constants = getattr(object_class, "constants", [])
    object_builtin.enums = getattr(object_class, "enums", [])
    object_builtin.methods = getattr(object_class, "methods", [])
    object_builtin.operators = getattr(object_class, "operators", [])
    # Add to builtins
    all_builtin_classes.append(object_builtin)




# ============= generate stub for dummy builtin classes in godot ============

import os

# 收集所有枚举（全局枚举 + 所有 class 的枚举）
all_enums = []  # (class_name, enum_obj)
for builtin in all_builtin_classes:
    if hasattr(builtin, 'enums') and builtin.enums:
        for enum in builtin.enums:
            all_enums.append((builtin.name, enum))
for cls in all_classes:
    if hasattr(cls, 'enums') and cls.enums:
        for enum in cls.enums:
            all_enums.append((cls.name, enum))


# Write global enums and all class enums to enums.pyi
enums_pyi_w = Writer()
enums_pyi_w.buffer += [
    'from enum import Enum',
    '',
]
for global_enum in all_global_enums:
    global_enum_to_pyi(global_enum, enums_pyi_w)
for class_name, enum in all_enums:
    enums_pyi_w.write(f'class {class_name}_{enum.name}(Enum):')
    enums_pyi_w.indent()
    if getattr(enum, 'description', None):
        enums_pyi_w.write(f'"""{enum.description}')
        enums_pyi_w.write(f'"""')
    if getattr(enum, 'values', None):
        for value in enum.values:
            enums_pyi_w.write(f'{value.name} = {value.value}')
    enums_pyi_w.dedent()
    enums_pyi_w.write('')
with open(STUB_ENUM_PATH, 'w', encoding='utf-8') as fp:
    fp.write(str(enums_pyi_w))

# Write builtin classes to builtins.pyi
builtins_pyi_w = Writer()
builtins_pyi_w.buffer += [
    "from typing import TypeVar, Generic",
    f"from {os.path.basename(STUB_ENUM_PATH).replace('.py', '')} import *",
    "",
    "class NativeBase: pass",
    "class BuiltinBase: pass",
    "",
    "T = TypeVar('T')",
    "",
    "class Signal(Generic[T]): pass",
    "",
    "intptr = int",
    "def default(comment: str): ...",
    "class Variant:",
    "    pass",
    "",
    ""
]
for single_builtin_class in all_builtin_classes:
    builtin_class_to_pyi(single_builtin_class, builtins_pyi_w)
with open(STUB_BUILTIN_PATH, 'w', encoding='utf-8') as fp:
    fp.write(str(builtins_pyi_w))

# Write native classes to natives.pyi
natives_pyi_w = Writer()
natives_pyi_w.buffer += [
    f'from {os.path.basename(STUB_ENUM_PATH).replace(".py", "")} import *',
    f'from .{os.path.basename(STUB_BUILTIN_PATH).replace(".pyi", "")} import *',
    "",
    "",
    "",
]
for single_class in all_classes:
    single_class_to_pyi(single_class, natives_pyi_w)
with open(STUB_NATIVE_PATH, 'w', encoding='utf-8') as fp:
    fp.write(str(natives_pyi_w))


with open(STUB_TYPING_INIT_PATH, 'w', encoding='utf-8') as fp:
    fp.write(f'''
from .{os.path.basename(STUB_BUILTIN_PATH).replace('.pyi', '')} import *
from .{os.path.basename(STUB_NATIVE_PATH).replace('.pyi', '')} import *
''')

# ============= generate stub for exposed godot api ============
# pyi_w = Writer()

# header = [
#     'from typing import TypeVar, Literal, overload',
#     '',
#     'T = TypeVar("T")',
#     '',
#     '',
#     'class ExtendsHint[T]:',
#     '    @property',
#     '    def owner(self) -> T: ...',
#     '',
# ]

# pyi_w.buffer += header



# # Define Extends function for each class
# def wrap_class(name: str, pyi_w: Writer):
#     pyi_w.write('@overload')
#     pyi_w.write(f'def Extends(cls: Literal[\'{name}\']) -> type[ExtendsHint[{name}]]: ...')

# for builtin_class in all_builtin_classes:
#     wrap_class(builtin_class.name, pyi_w)

# for single_class in all_classes:
#     wrap_class(single_class.name, pyi_w)


# # Define group size for splitting classes
# GROUP_SIZE = 50

# # Split builtin classes into groups
# builtin_class_groups = []
# for i in range(0, len(all_builtin_classes), GROUP_SIZE):
#     group = all_builtin_classes[i:i+GROUP_SIZE]
#     builtin_class_groups.append(group)

# # Split native classes into groups
# native_class_groups = []
# for i in range(0, len(all_classes), GROUP_SIZE):
#     group = all_classes[i:i+GROUP_SIZE]
#     native_class_groups.append(group)

# # Generate Literal types for each group
# for i, group in enumerate(builtin_class_groups):
#     class_list_str = ', '.join([f"'{c.name}'" for c in group])
#     pyi_w.write(f"BuiltinClassGroup{i} = Literal[{class_list_str}]")

# for i, group in enumerate(native_class_groups):
#     class_list_str = ', '.join([f"'{c.name}'" for c in group])
#     pyi_w.write(f"CGNativeClassGroup{i} = Literal[{class_list_str}]")

# # Create union types for all groups
# builtin_groups_union = ' | '.join([f"BuiltinClassGroup{i}" for i in range(len(builtin_class_groups))])
# native_groups_union = ' | '.join([f"CGNativeClassGroup{i}" for i in range(len(native_class_groups))])

# pyi_w.write(f"BuiltinClass = {builtin_groups_union}")
# pyi_w.write(f"CGNativeClass = {native_groups_union}")

# # Define export function
# pyi_w.write('@overload')
# pyi_w.write('def export(cls: BuiltinClass): ...')
# pyi_w.write('@overload')
# pyi_w.write('def Extends(cls: CGNativeClass): ...')



#### 6/23 ####



pyi_w = Writer()
pyi_w.write(f'''
from typing import TypeVar
from {os.path.basename(STUB_ENUM_PATH).replace('.py', '')} import *
from typings import *


class GDBuiltinClass[T: BuiltinBase]:
    def __init__(self, name: str): ...

class GDNativeClass[T: NativeBase]:
    def __init__(self, name: str): ...

class ExtendsHint[T: BuiltinBase | NativeBase]:
    @property
    def owner(self) -> T: ...

def Extends[T: NativeBase](cls: GDNativeClass[T]) -> type[ExtendsHint[T]]: ...

# e.g.
Resource = GDNativeClass[Resource]('Resource')

''')




with open(EXPOSED_STUB_PATH, 'w', encoding='utf-8') as fp:
    fp.write(str(pyi_w))
