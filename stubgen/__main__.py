# from .schema import load_extension_api, ClassesSingle, BuiltinClass, GlobalEnum
# from keyword import iskeyword

# BUILTIN_TYPES = {
#     'None', 'int', 'float', 'bool', 'str'
# }

# class Writer:
#     def __init__(self) -> None:
#         self.buffer = []
#         self.indent_level = 0

#     def indent(self):
#         self.indent_level += 1

#     def dedent(self):
#         self.indent_level -= 1

#     def write(self, line: str):
#         self.buffer.append('    ' * self.indent_level + line)

#     def __str__(self) -> str:
#         return '\n'.join(self.buffer)

# def wrap_builtin_type(t: str, need_quote: bool=True):
#     if t in BUILTIN_TYPES:
#         return t
#     else:
#         t = t.replace('enum::', '')
#         t = t.replace('.', '_')
#         t = t.replace('bitfield::', '')  # v2 bitfield::xxx -> xxx
#         t = 'int' if "*" in t else t  # v2 intptr -> int
#         t = t.replace('typedarray::', 'list[') + ']' if 'typedarray::' in t else t  # v2 typedarray::xxx -> list[xxx]
#         t = t.split(',')[0] if "," in t else t  # v2 BaseResourceClass,ResourceClass -> BaseResource
#         return f'\'{t}\'' if need_quote else f'{t}'
    
# def wrap_default_value(t: str):
#     if t == 'true':
#         return f'True'
#     if t == 'false':
#         return f'False'
#     t = t.replace('\\', '\\\\')
#     t = t.replace('"', '\\"')
#     if '()' in t:
#         return f'{t}'
#     try:
#         return int(t)
#     except ValueError:
#         try:
#             return float(t)
#         except ValueError:        
#             return f'\'{t}\''

# def wrap_keyword(t: str):
#     if iskeyword(t):
#         return f'{t}_'
#     return f'{t}'

# def global_enum_to_pyi(global_enum: GlobalEnum, pyi_w: Writer) -> None:
#     assert pyi_w.indent_level == 0
#     pyi_w.write(f'class {wrap_builtin_type(global_enum.name, False)}:')
#     pyi_w.indent()
#     for e in global_enum.values:
#         pyi_w.write(f'{e.name} = {e.value}')
#     pyi_w.write('')
#     pyi_w.dedent()
    

# def single_builtin_class_to_pyi(single_class: BuiltinClass, pyi_w: Writer) -> None:
#     assert pyi_w.indent_level == 0
#     pyi_w.write(f'class {single_class.name}:')
#     pyi_w.indent()
#     pyi_w.write('pass')
#     pyi_w.write('')
#     pyi_w.dedent()
 
# def single_class_to_pyi(single_class: ClassesSingle, pyi_w: Writer) -> None:
#     assert pyi_w.indent_level == 0
#     has_properties = False
#     has_constants = False
#     has_signals = False
#     has_methods = False
#     # class xxx:
#     if single_class.inherits is None:
#         pyi_w.write(f'class {single_class.name}:')
#     else:
#         pyi_w.write(f'class {single_class.name}({single_class.inherits}):')
#     pyi_w.indent()
#     # Add multi row comment
#     description = ''
#     if single_class.brief_description:
#         description += single_class.brief_description
#         description += '\t\n'
#     if single_class.description:
#         description += single_class.description
#         description += '\t\n'
#     if description:
#         pyi_w.write(f'"""{description}')
#         pyi_w.write(f'"""')
#     # properties, xxx: type
#     if single_class.properties:
#         has_properties = True
#         for p in single_class.properties:
#             pyi_w.write(f'{wrap_keyword(p.name)}: {wrap_builtin_type(p.type)}')
#     # constants, xxx = value
#     if single_class.constants:
#         has_constants = True
#         for c in single_class.constants:
#             pyi_w.write(f'{wrap_keyword(c.name)} = {c.value}')
#         pyi_w.write('')
#     # signals, xxx = signal()
#     if single_class.signals:
#         has_signals = True
#         for s in single_class.signals:
#             pyi_w.write(f'{wrap_keyword(s.name)} = signal()')
#     # methods, and @staticmethod
#     if single_class.methods:
#         has_methods = True
#         for m in single_class.methods:
#             static_flag = m.is_static
#             vararg_flag = m.is_vararg
#             # make argument str, xx: type=val
#             arg_list = []
#             arg_self_str = 'self'
#             arg_varg_str = '*arg'
#             if m.arguments:
#                 arg_self_str = 'self, '
#                 arg_varg_str = ', *arg'
#                 for arg in m.arguments:
#                     arg_val = ''
#                     arg_val += f'{wrap_keyword(arg.name)}: {wrap_builtin_type(arg.type)}'
#                     if arg.default_value:
#                         arg_val += f' = {wrap_default_value(arg.default_value)}'
#                     arg_list.append(arg_val)
#             arg_str = ', '.join(arg_list)
#             # add @staticmethod
#             if static_flag == True:
#                 pyi_w.write(f'@staticmethod')
#             # add 'self' for general methods
#             else:
#                 arg_str = arg_self_str + arg_str
#             # add *arg
#             if vararg_flag == True:
#                 arg_str += arg_varg_str
#             # special case
#             if arg_str == 'self*arg':
#                 arg_str = 'self, *arg'
#             return_val = 'None'
#             if m.return_value:
#                 return_val = m.return_value.type
#             pyi_w.write(f'def {wrap_keyword(m.name)}({arg_str}) -> {wrap_builtin_type(return_val)}: ...')
#             method_description = ''
#             if m.description:
#                 method_description = m.description
#                 pyi_w.indent()
#                 pyi_w.write(f'"""{method_description}')
#                 pyi_w.write(f'"""')
#                 pyi_w.dedent()
#     if (has_methods or has_constants or has_properties or has_signals) == False:
#         pyi_w.write('pass')
#     pyi_w.write('')
#     pyi_w.dedent()
#     # enums, create new class
#     if single_class.enums:
#         for e in single_class.enums:
#             pyi_w.write(f'class {single_class.name}_{e.name}(Enum):')
#             pyi_w.indent()
#             enum_description = ''
#             if e.description:
#                 enum_description = e.description
#                 pyi_w.write(f'"""{enum_description}')
#                 pyi_w.write(f'"""')
#             if e.values:
#                 for value in e.values:
#                     pyi_w.write(f'{value.name} = {value.value}')
#             pyi_w.dedent()
#             pyi_w.write('')
                
# all_in_one = load_extension_api('godot-cpp/gdextension/extension_api.json')
# all_global_enums = all_in_one.global_enums
# all_builtin_classes = all_in_one.builtin_classes
# all_classes = all_in_one.classes

# pyi_w = Writer()



# headers = [
#     'from enum import Enum',
#     # 空两行
#     "",
#     "",
# ]
# pyi_w.buffer += headers

# for global_enum in all_global_enums:
#     global_enum_to_pyi(global_enum, pyi_w)

# for single_builtin_class in all_builtin_classes:
#     single_builtin_class_to_pyi(single_builtin_class, pyi_w)

# for single_class in all_classes:
#     single_class_to_pyi(single_class, pyi_w)

# with open('typings/godot_class.pyi', 'w', encoding='utf-8') as fp:
#     fp.write(str(pyi_w))


from attr import dataclass
from .schema import load_extension_api, ClassesSingle, BuiltinClass, GlobalEnum, builtin_class_to_classes_single
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
    return f'default({t})'


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
    

def builtin_class_to_pyi(single_class: BuiltinClass, pyi_w: Writer) -> None:
    assert pyi_w.indent_level == 0
    if single_class.name == "Variant":
        single_class.inherits = None
    
    # Convert BuiltinClass to ClassesSingle and use the same processing function
    classes_single = builtin_class_to_classes_single(single_class)
    single_class_to_pyi(classes_single, True, pyi_w)
 
def single_class_to_pyi(single_class: ClassesSingle, is_builtin_class: bool, pyi_w: Writer) -> None:
    assert pyi_w.indent_level == 0
    has_properties = False
    has_constants = False
    has_signals = False
    has_methods = False
    has_operators = False
    # class xxx:
    if single_class.inherits is None:
        pyi_w.write(f'class {single_class.name}:')
    else:
        pyi_w.write(f"class {single_class.name}('{single_class.inherits}'):")
    pyi_w.indent()
    # Add multi row comment
    description = ''
    if single_class.brief_description:
        description += single_class.brief_description
        description += '\t\n'
    if single_class.description:
        description += single_class.description
        description += '\t\n'
    if description:
        pyi_w.write(f'"""{description}')
        pyi_w.write(f'"""')
    # properties, xxx: type (ClassesSingle only)
    if not is_builtin_class:
        if single_class.properties:
            has_properties = True
            for p in single_class.properties:
                pyi_w.write(f'{wrap_keyword(p.name)}: {wrap_builtin_type(p.type)}')
    # constants, xxx = value
    if single_class.constants:
        has_constants = True
        for c in single_class.constants:
            if isinstance(c.value, str):
                c.value = c.value.replace('inf', "float('inf')")
            pyi_w.write(f'{wrap_keyword(c.name)} = {wrap_value(c.value, [c]).result}')
        pyi_w.write('')
    # signals  (ClassesSingle only)
    if not is_builtin_class:
        if single_class.signals:
            has_signals = True
            for s in single_class.signals:
                if s.arguments:
                    args = ", ".join([f"'{arg.type}'" for arg in s.arguments])
                    args_in_comment = ", ".join([f"{arg.name}: {wrap_builtin_type(arg.type)}" for arg in s.arguments])
                    pyi_w.write(f'{wrap_keyword(s.name)}: Signal[Callable[[{args}], None]]  # {s.name}({args_in_comment})')
                else:
                    pyi_w.write(f'{wrap_keyword(s.name)}: Signal[Callable[[], None]]  # {s.name}()')
    # operators (BuiltinClass only)
    if is_builtin_class:
        if single_class.operators:
            has_operators = True
            for o in single_class.operators:
                if o.name in NOT_SUPPORTED_OPERATORS:
                    continue
                if o.name in OPERATORS_TABLE:
                    if o.right_type:
                        pyi_w.write(f'def {OPERATORS_TABLE[o.name]}(self, other: {wrap_builtin_type(o.right_type)}) -> {wrap_builtin_type(o.return_type)}: ...')
                    else:
                        pyi_w.write(f'def {OPERATORS_TABLE[o.name]}(self) -> {wrap_builtin_type(o.return_type)}: ...')
                else:
                    raise Exception(f'发现新的运算符: {o.name}')
        
        
    # methods
    if single_class.methods:
        has_methods = True
        for m in single_class.methods:
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
                    if arg.default_value:
                        default_value_dataclass = wrap_value(arg.default_value, [arg])
                        add_None = default_value_dataclass.add_None
                        default_value_str = f' = {default_value_dataclass.result}'
                    arg_val += f'{wrap_keyword(arg.name)}: {wrap_builtin_type(arg.type)}{"|None" if add_None else ""}'
                    if arg.default_value:
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
            return_val = 'None'
            # if m.return_value:
            #     return_val = m.return_value.type
            pyi_w.write(f'def {wrap_keyword(m.name)}({arg_str}) -> {wrap_builtin_type(return_val)}: ...')
            method_description = ''
            if m.description:
                method_description = m.description
                pyi_w.indent()
                pyi_w.write(f'"""{method_description}')
                pyi_w.write(f'"""')
                pyi_w.dedent()
    if (has_methods or has_constants or has_properties or has_signals or has_operators) == False:
        pyi_w.write('pass')
    pyi_w.write('')
    pyi_w.dedent()
    # enums, create new class
    if single_class.enums:
        for e in single_class.enums:
            pyi_w.write(f'class {single_class.name}_{e.name}(Enum):')
            pyi_w.indent()
            enum_description = ''
            if e.description:
                enum_description = e.description
                pyi_w.write(f'"""{enum_description}')
                pyi_w.write(f'"""')
            if e.values:
                for value in e.values:
                    pyi_w.write(f'{value.name} = {value.value}')
            pyi_w.dedent()
            pyi_w.write('')
            
all_in_one = load_extension_api(EXTENSION_API_PATH)
all_global_enums = all_in_one.global_enums
all_builtin_classes = all_in_one.builtin_classes
all_classes = all_in_one.classes

pyi_w = Writer()



headers = [
    'from enum import Enum',
    "from typing import Callable",
    # 空两行
    "",
    "",
    "intptr = int",
    "def default(comment: str): ..."
    "class Variant:",
    "    pass",
]
pyi_w.buffer += headers

for global_enum in all_global_enums:
    global_enum_to_pyi(global_enum, pyi_w)

for single_builtin_class in all_builtin_classes:
    builtin_class_to_pyi(single_builtin_class, pyi_w)

for single_class in all_classes:
    single_class_to_pyi(single_class, False, pyi_w)

with open(STUB_PATH, 'w', encoding='utf-8') as fp:
    fp.write(str(pyi_w))
    
