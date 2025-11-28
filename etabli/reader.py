from functools import reduce
from operator import or_
from pathlib import Path

import tomllib


def read_toml_data(path: Path, first_call=True) -> dict:
    """Read a toml file, or a nested directory of files

    Only reads files with ".toml" extension. Returns a nested dictionary from dir and file names, and file data.
    """
    if path.is_file():
        if path.suffix == ".toml":
            return {path.stem: tomllib.loads(path.read_text())}
        else:
            return {}
    elif path.is_dir():
        # recursive call. join data from files and subdirs
        data = reduce(
            or_,
            (read_toml_data(subpath, first_call=False) for subpath in path.iterdir()),
            {},
        )
        if first_call:
            # first level of data has no name
            return data
        else:
            # when recursing into files and subdirs, name dict from file or dir name
            return {path.name: data}
    else:
        raise RuntimeError(f"path not supported: {path}")
