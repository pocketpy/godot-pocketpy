from .schema_gdt import GlobalEnum, ClassesEnum, BuiltinClassEnum
from .writer import Writer
from typing import Any

def _gen_raw_enums(w: Writer, name: str, values: list[tuple[str, Any]], is_bitfield: bool, with_types=True, with_values=True) -> None:
    if with_types:
        if is_bitfield:
            w.write(f"{name} = int")
        else:
            literal_values = [str(v) for _, v in values]
            w.write(f"{name} = Literal[{', '.join(literal_values)}]")
    if with_values:
        for k, v in values:
            w.write(f"{k} = {v}")
    w.write('')


def gen_global_enums(w: Writer, global_enums: list[GlobalEnum], with_types: bool, with_values: bool) -> None:
    for e in global_enums:
        name = e.name.replace('.', '_')
        _gen_raw_enums(w, name, [
            (v.name, v.value) for v in e.values
        ], e.is_bitfield, with_types, with_values)

def gen_class_enum(w: Writer, e: ClassesEnum):
    assert e.values is not None
    _gen_raw_enums(w, e.name, [
        (v.name, v.value) for v in e.values
    ], e.is_bitfield)

def gen_builtin_class_enum(w: Writer, e: BuiltinClassEnum):
    assert e.values is not None
    _gen_raw_enums(w, e.name, [
        (v.name, v.value) for v in e.values
    ], False)