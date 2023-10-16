import inspect
import sys
from functools import wraps
from logging import getLogger

from rich import print

from etabli.persistance import dump_pickle

logger = getLogger(__name__)


def calling_function():
    return inspect.stack()[2].function


def print_call(func):
    """Print function call string"""

    @wraps(func)
    def wrapped(*args, **kwargs):
        args_string = ",".join(repr(arg) for arg in args)
        kwargs_string = ",".join(f"{k}={repr(v)}" for k, v in kwargs.items())

        result = func(*args, **kwargs)
        print(f"{func.__name__}({args_string!r},{kwargs_string!r}) -> {result!r}")
        return result

    return wrapped


def save_call(func):
    @wraps(func)
    def wrapped(*args, save_replay=True, **kwargs):
        if save_replay:
            replay = (func.__module__, func.__name__, args, kwargs)
            dump_pickle(replay, "replay.pkl")
            logger.critical("function call saved, aborting everything")
            sys.exit()
        return func(*args, **kwargs)

    wrapped.has_replay = True
    return wrapped
