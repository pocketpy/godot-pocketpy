from .schema_gdt import *
from .schema_py import PyType

def parse_to_gdt_schema(extension_api_path: str):
    all_in_one = load_extension_api(extension_api_path)

    for clazz in all_in_one.builtin_classes:
        if clazz.name != 'Object':
            PyType.NO_OBJECT_VARIANT_TYPES.add(clazz.name)
    return all_in_one