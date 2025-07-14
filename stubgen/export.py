# from .schema_py import *
from .writer import Writer

# def export_pyi(pyfile: PyFile, filepath: str):
#     lines = PyFile.convert_to_lines(pyfile, wrap_with_single_quote=False)
#     with open(filepath, 'w', encoding='utf-8') as f:
#         f.write('\n'.join(lines))

def export_writer(w: Writer, filepath: str, mode: str = 'w'):
    with open(filepath, mode, encoding='utf-8') as f:
        f.write(str(w))