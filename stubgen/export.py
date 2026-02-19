import os
from .writer import Writer

def export_writer(w: Writer, filepath: str, mode: str = 'w'):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode, encoding='utf-8') as f:
        f.write(str(w))
