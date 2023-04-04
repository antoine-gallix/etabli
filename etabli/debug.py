import logging
import os
from pprint import pformat, pprint

from pathlib import Path


# -----------------------------------------------


def unbuffered_file(filename):
    return Path(filename).open("w", buffering=1)


class File_Writer:
    def __init__(self, filename):
        # unbuffered file allows real time following the file
        self.file = unbuffered_file(filename)

    def write(self, thing):
        """write a line to the file"""

        self.file.write(thing + "\n")


def file_logger_factory(file, name):
    """Create a logger that writes to a file
    """
    formatter = logging.Formatter("%(message)s")

    handler = logging.FileHandler(file, mode="w")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger


def arguments():
    """Returns tuple containing dictionary of calling function's
       named arguments and a list of calling function's unnamed
       positional arguments.
    """
    from inspect import getargvalues, stack

    posname, kwname, args = getargvalues(stack()[1][0])[-3:]
    posargs = args.pop(posname, [])
    args.update(args.pop(kwname, []))
    return args, posargs


def status():
    fargs = arguments()
    print(fargs["args"])
    print(fargs["kwargs"])


def print_factory(file):
    "Create functions that print to a file"

    def print_to_file(s=None):
        if s is None:
            to_print = ''
        elif isinstance(s, str):
            to_print = s
        else:
            to_print = pformat(s)
        print(to_print, flush=True, file=file)

    return print_to_file


def print_at_level(s, n):
    print(n * "\t", end="")
    print(s)


class Printer:
    def __init__(self):
        self._indent = 0

    def __call__(self, s):
        self.print(s)

    def indent(self, n=None):
        if n is None:
            self._indent += 1
        else:
            self._indent += n

    def dedent(self):
        self._indent = max(self._indent - 1, 0)

    def reset_indent(self):
        self._indent = 0

    def print(self, s, prefix=None):
        prefix = prefix or ''
        print(f'{" "*4*self._indent}{prefix}{str(s)}')

    def iter(self, iterable, **kwargs):
        for i in iterable:
            self.print(i, **kwargs)
