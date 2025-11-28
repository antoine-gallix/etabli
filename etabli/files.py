from pathlib import Path

import arrow
from rich import print
from rich.text import Text


def resolve_path(path: Path | str):
    return Path(path).expanduser().resolve()


def walk_files(path: Path | str):
    """Yield files recursively from a directory"""
    path = resolve_path(path)
    for path, _, files in path.walk():
        for file in files:
            yield path / file


def is_name_hidden(path: Path):
    """Name of file or dir has hidden pattern"""
    return str(path.name).startswith(".")


def is_hidden(path: Path):
    """File or dir is hidden, or has a hidden parent dir"""
    return is_name_hidden(path) or any(map(is_name_hidden, path.parents))


def day_timestamp():
    return arrow.now().format("YYYY-MM-DD")


def style_dir(path):
    return Text(str(path), style="green")


def style_file(path):
    return Text(str(path), style="blue")


def style_path(path):
    if path.is_file():
        return style_file(path)
    elif path.is_dir():
        return style_dir(path)
    else:
        return Text(str(path))


def ensure_dir_exists(dir_path: Path):
    print(f"ensure destination exists: {style_path(dir_path)}")
    dir_path.mkdir(parents=True, exist_ok=True)
