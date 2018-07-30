from os.path import split
from os.path import isfile
import pickle
import json
from pathlib import Path
import dictdiffer
from pprint import pprint

# ---------------------pickle---------------------


def dump_pickle(thing,path):
    """a pickle wrapper
    """
    output=Path(path)
    output.write_bytes(pickle.dumps(thing))
    print(f"saved pickle to '{output}'")


def load_pickle(path):
    input=Path(path)
    thing = pickle.loads(input.read_bytes())
    print(f"loaded pickle from '{input}'")
    return thing

# ---------------------json---------------------


def load_json(path):
    input=Path(path)
    print(f'loading json from {path}')
    try:
        thing = json.loads(input.read_text())
    except json.decoder.JSONDecodeError as e:
        print('error while loading json')
    return thing

