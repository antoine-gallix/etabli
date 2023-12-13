import importlib

from etabli.persistance import load_pickle

module_name, function_name, args, kwargs = load_pickle("replay.pkl")
module = importlib.import_module(module_name)
function = getattr(module, function_name)
if hasattr(function, "has_replay"):
    function(*args, save_replay=False, **kwargs)
else:
    function(*args, **kwargs)
