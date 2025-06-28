from stubgen.parse import *
from stubgen.map import *
from stubgen.export import *
import os



EXTENSION_API_PATH = 'godot-cpp/gdextension/extension_api.json'



gdt_schema = parse_to_gdt_schema(EXTENSION_API_PATH)
map_result = map_gdt_to_py(gdt_schema)

GODOT_TYPINGS_PATH = 'typings/godot/'
os.makedirs(GODOT_TYPINGS_PATH, exist_ok=True)
export_pyi(map_result.typings_pyi, GODOT_TYPINGS_PATH + 'typings.pyi')
export_pyi(map_result.enum_pyi, GODOT_TYPINGS_PATH + 'enum.pyi')
export_pyi(map_result.init_pyi, GODOT_TYPINGS_PATH + '__init__.pyi')