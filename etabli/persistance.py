import json
import pickle
from os.path import isfile, split
from pathlib import Path
from pprint import pprint

# ---------------------pickle---------------------


def dump_pickle(thing, path):
    """a pickle wrapper
    """
    output_path = Path(path).expanduser()
    output_path.parent.mkdir(exist_ok=True,parents=True)
    output_path.write_bytes(pickle.dumps(thing))
    print(f"saved pickle to '{output_path}'")


def load_pickle(path):
    input_path = Path(path).expanduser()
    thing = pickle.loads(input_path.read_bytes())
    print(f"loaded pickle from '{input_path}'")
    return thing


# ---------------------json---------------------


def load_json(path):
    input = Path(path)
    print(f'loading json from {path}')
    try:
        thing = json.loads(input.resolve().read_text())
    except json.decoder.JSONDecodeError as e:
        print('error while loading json')
    return thing


# ---------------------write to file---------------------


def write_to_file(s, path):
    """write a string to a file
    """

    file = Path(path).resolve()
    file.write_text(s)
    print(f'written {len(s)} chars to {file}')


def read_from_file(path):
    """read a file content
    """
    file = Path(path).resolve()
    s = file.read_text()
    print(f'read {len(s)} chars to {file}')
    return s
