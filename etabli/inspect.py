import inspect
from functools import wraps


def calling_function():
    return inspect.stack()[2].function

def print_call(func):
    """Print function call string"""
    @wraps(func)
    def wrapped(*args, **kwargs):
        args_string = ",".join(repr(arg) for arg in args)
        kwargs_string = ",".join(f"{k}={repr(v)}" for k, v in kwargs.items())

        print(f"{func.__name__}({args_string},{kwargs_string})")
        return func(*args, **kwargs)

    return wrapped
