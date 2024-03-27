import inspect
import sys
from functools import wraps
from logging import getLogger

import funcy
import rich
from rich import print

from etabli.persistance import dump_pickle

logger = getLogger(__name__)


def calling_function():
    return inspect.stack()[2].function


def print_call(func):
    """Print function call string"""

    @wraps(func)
    def wrapped(*args, **kwargs):
        pargs_string = ",".join(repr(arg) for arg in args)
        kwargs_string = ",".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        args_string = ",".join(funcy.keep((pargs_string, kwargs_string)))
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__}({args_string}) -> {result!r}")
            return result
        except Exception as exc:
            print(f"{func.__name__}({args_string}) ! {exc.__class__.__name__}:{exc}")
            raise

    return wrapped


def inspect_exception(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            rich.inspect(exc)
            raise

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
