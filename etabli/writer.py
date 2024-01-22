from pathlib import Path


class Composer:
    def __init__(self):
        self.lines = []

    def __str__(self):
        return "\n".join(self.lines)

    def add(self, line):
        self.lines.append(line)

    def newline(self):
        self.lines.append("")

    def write(self, path):
        print(f"writing content into {path}")
        Path(path).write_text(str(self))
