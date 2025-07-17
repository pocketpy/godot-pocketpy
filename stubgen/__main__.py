from stubgen.parse import *
from stubgen.map import *
from stubgen.export import *
import os
import shutil


EXTENSION_API_PATH = 'godot-cpp/gdextension/extension_api.json'



gdt_schema = parse_to_gdt_schema(EXTENSION_API_PATH)
map_result = map_gdt_to_py(gdt_schema)

TYPINGS_PATH = 'demo/addons/godot-pocketpy/typings'
GODOT_TYPINGS_PATH = f'{TYPINGS_PATH}/godot'
shutil.rmtree(TYPINGS_PATH, ignore_errors=True)
shutil.copytree('pocketpy/include/typings', TYPINGS_PATH)
os.mkdir(GODOT_TYPINGS_PATH)

export_writer(map_result.enums_pyi, f'{GODOT_TYPINGS_PATH}/enums.pyi')
export_writer(map_result.init_pyi, f'{GODOT_TYPINGS_PATH}/__init__.pyi')
export_writer(map_result.c_writer, 'src/lang/BindingsGenerated.cpp')
export_writer(map_result.typings_pyi, f'{GODOT_TYPINGS_PATH}/classes.pyi')
export_writer(map_result.alias_pyi, f'{GODOT_TYPINGS_PATH}/alias.pyi')
export_writer(map_result.header_pyi, f'{GODOT_TYPINGS_PATH}/header.pyi')
