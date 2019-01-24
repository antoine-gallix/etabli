import json
import pickle
from os.path import isfile, split
from pprint import pprint

from pathlib import Path


# ---------------------pickle---------------------


def dump_pickle(thing, path):
    """a pickle wrapper
    """
    output = Path(path)
    output.write_bytes(pickle.dumps(thing))
    print(f"saved pickle to '{output}'")


def load_pickle(path):
    input = Path(path)
    thing = pickle.loads(input.read_bytes())
    print(f"loaded pickle from '{input}'")
    return thing


# ---------------------json---------------------


def load_json(path):
    input = Path(path)
    print(f'loading json from {path}')
    try:
        thing = json.loads(input.read_text())
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
