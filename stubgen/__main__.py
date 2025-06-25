from .schema import load_extension_api, ClassesSingle, BuiltinClass, GlobalEnum
from keyword import iskeyword

BUILTIN_TYPES = {
    'None', 'int', 'float', 'bool', 'str'
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
        t = 'int' if "*" in t else t  # v2 intptr -> int
        t = t.replace('typedarray::', 'list[') + ']' if 'typedarray::' in t else t  # v2 typedarray::xxx -> list[xxx]
        t = t.split(',')[0] if "," in t else t  # v2 BaseResourceClass,ResourceClass -> BaseResource
        return f'\'{t}\'' if need_quote else f'{t}'
    
def wrap_default_value(t: str):
    if t == 'true':
        return f'True'
    if t == 'false':
        return f'False'
    t = t.replace('\\', '\\\\')
    t = t.replace('"', '\\"')
    if '()' in t:
        return f'{t}'
    try:
        return int(t)
    except ValueError:
        try:
            return float(t)
        except ValueError:        
            return f'\'{t}\''

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
    

def single_builtin_class_to_pyi(single_class: BuiltinClass, pyi_w: Writer) -> None:
    assert pyi_w.indent_level == 0
    pyi_w.write(f'class {single_class.name}:')
    pyi_w.indent()
    pyi_w.write('pass')
    pyi_w.write('')
    pyi_w.dedent()
 
def single_class_to_pyi(single_class: ClassesSingle, pyi_w: Writer) -> None:
    assert pyi_w.indent_level == 0
    has_properties = False
    has_constants = False
    has_signals = False
    has_methods = False
    # class xxx:
    if single_class.inherits is None:
        pyi_w.write(f'class {single_class.name}:')
    else:
        pyi_w.write(f'class {single_class.name}({single_class.inherits}):')
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
    # properties, xxx: type
    if single_class.properties:
        has_properties = True
        for p in single_class.properties:
            pyi_w.write(f'{wrap_keyword(p.name)}: {wrap_builtin_type(p.type)}')
    # constants, xxx = value
    if single_class.constants:
        has_constants = True
        for c in single_class.constants:
            pyi_w.write(f'{wrap_keyword(c.name)} = {c.value}')
        pyi_w.write('')
    # signals, xxx = signal()
    if single_class.signals:
        has_signals = True
        for s in single_class.signals:
            pyi_w.write(f'{wrap_keyword(s.name)} = signal()')
    # methods, and @staticmethod
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
                    arg_val += f'{wrap_keyword(arg.name)}: {wrap_builtin_type(arg.type)}'
                    if arg.default_value:
                        arg_val += f' = {wrap_default_value(arg.default_value)}'
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
            if m.return_value:
                return_val = m.return_value.type
            pyi_w.write(f'def {wrap_keyword(m.name)}({arg_str}) -> {wrap_builtin_type(return_val)}: ...')
            method_description = ''
            if m.description:
                method_description = m.description
                pyi_w.indent()
                pyi_w.write(f'"""{method_description}')
                pyi_w.write(f'"""')
                pyi_w.dedent()
    if (has_methods or has_constants or has_properties or has_signals) == False:
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
                
all_in_one = load_extension_api('godot-cpp/gdextension/extension_api.json')
all_global_enums = all_in_one.global_enums
all_builtin_classes = all_in_one.builtin_classes
all_classes = all_in_one.classes

pyi_w = Writer()



headers = [
    'from enum import Enum',
    # 空两行
    "",
    "",
]
pyi_w.buffer += headers

for global_enum in all_global_enums:
    global_enum_to_pyi(global_enum, pyi_w)

for single_builtin_class in all_builtin_classes:
    single_builtin_class_to_pyi(single_builtin_class, pyi_w)

for single_class in all_classes:
    single_class_to_pyi(single_class, pyi_w)

with open('typings/godot_class.pyi', 'w', encoding='utf-8') as fp:
    fp.write(str(pyi_w))
    
