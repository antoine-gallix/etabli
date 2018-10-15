import logging
import os
from pathlib import Path
from icecream import ic


# logger that prints to a file

debug_logger_name = 'debug'
debug_log_file = os.environ.get('DEBUG_LOG_FILE')
ic_log_to_file = os.environ.get('IC_LOG_TO_FILE')

# -----------------------------------------------


class File_Writer:
    def __init__(self, file):
        self.file = Path(file).open('w')

    def write(self, thing):
        self.file.write(thing + '\n')


def file_logger_factory(file, name):
    """Create a logger that writes to a file
    """

    logger = logging.getLogger(name)
    handler = logging.FileHandler(debug_log_file, mode='w')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
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
    print(fargs['args'])
    print(fargs['kwargs'])

# ---------------setup IC--------------


ic_config = {'prefix': ''}
if ic_log_to_file:
    writer = File_Writer(debug_log_file)
    ic_config.update({'outputFunction': writer.write})
ic.configureOutput(**ic_config)
