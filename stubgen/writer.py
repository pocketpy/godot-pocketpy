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
        return self
    
    def writefmt(self, fmt: str, *args):
        self.write(fmt.format(*args))

    def __str__(self) -> str:
        return '\n'.join(self.buffer)