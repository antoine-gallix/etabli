import inspect


def calling_function():
    return inspect.stack()[1].function
