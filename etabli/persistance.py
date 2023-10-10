import json
import pickle
from pathlib import Path


def expand_path(path):
    """Expand path to full form"""
    return Path(path).expanduser().resolve()


# ---------------------pickle---------------------


def dump_pickle(thing, path):
    """a pickle wrapper"""
    output_path = expand_path(path)
    output_path.parent.mkdir(exist_ok=True, parents=True)
    output_path.write_bytes(pickle.dumps(thing))
    print(f"saved pickle to '{output_path}'")


def load_pickle(path):
    input_path = expand_path(path)
    thing = pickle.loads(input_path.read_bytes())
    print(f"loaded pickle from '{input_path}'")
    return thing


# ---------------------json---------------------


def load_json(path):
    input = expand_path(path)
    print(f"loading json data from {path}")
    try:
        return json.loads(input.read_text())
    except json.decoder.JSONDecodeError as e:
        print(f"error while loading file: {e}")
        raise


# ---------------------write to file---------------------


def write_to_file(s, path):
    """write a string to a file"""

    file = expand_path(path)
    file.write_text(s)
    print(f"written {len(s)} chars to {file}")


def read_from_file(path):
    """read a file content"""
    file = expand_path(path)
    s = file.read_text()
    print(f"read {len(s)} chars to {file}")
    return s
