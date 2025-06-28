from .schema_py import *

def export_pyi(pyfile: PyFile, filepath: str):
    lines = PyFile.convert_to_lines(pyfile)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
