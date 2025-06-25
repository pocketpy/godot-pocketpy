from .parse import *
from .map import *
from .export import *



EXTENSION_API_PATH = 'godot-cpp/gdextension/extension_api.json'

gdt_schema = parse_to_gdt_schema(EXTENSION_API_PATH)
pyfiles = map_gdt_to_py(gdt_schema)
for pyfile in pyfiles:
    export_pyi(pyfile, f'{pyfile.name}.pyi')