from .schema_gdt import *

def parse_to_gdt_schema(extension_api_path: str):
    all_in_one = load_extension_api(extension_api_path)
    return all_in_one