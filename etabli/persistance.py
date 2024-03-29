import datetime
import json
import pickle
from pathlib import Path
import arrow


class TimestampEncoder(json.JSONEncoder):
    """Convert datetime into iso strings"""

    def default(self, o):
        if isinstance(o, (datetime.datetime, datetime.date, datetime.time)):
            return o.isoformat()
        else:
            return super().default(o)


def expand_path(path) -> Path:
    """Expand path to full form"""
    return Path(path).expanduser().resolve()


# ---------------------pickle---------------------
def default_dump(extension):
    return f"etabli_dump_{arrow.utcnow().format('YYYYMMDDHHmmss')}.{extension}"


def dump_pickle(thing, path=None) -> None:
    """a pickle wrapper"""
    path = path or default_dump("pkl")
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


def dump_json(thing, path=None, encoder=None) -> None:
    path = path or default_dump("json")
    output_path: Path = expand_path(path)
    output_path.parent.mkdir(exist_ok=True, parents=True)
    output_path.write_text(json.dumps(thing, cls=encoder, indent=4))
    print(f"saved json data to {path}")


def load_json(path):
    full_path: Path = expand_path(path)
    print(f"loading json data from {full_path}")
    try:
        return json.loads(full_path.read_text())
    except json.decoder.JSONDecodeError as e:
        print(f"error while loading file: {e}")
        raise


# ---------------------write to file---------------------


def write_to_file(s, path) -> None:
    """write a string to a file"""

    file = expand_path(path)
    file.write_text(s)
    print(f"written {len(s)} chars to {file}")


def read_from_file(path) -> str:
    """read a file content"""
    file = expand_path(path)
    s = file.read_text()
    print(f"read {len(s)} chars to {file}")
    return s
