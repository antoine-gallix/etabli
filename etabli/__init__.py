# import os

# all those imports allows `from dev_tools import *` and have a lot of things in
# the namespace to quick debug
# from pdb import set_trace as bp  # noqa
# from pprint import pformat as pf  # noqa
# from pprint import pprint as ppr  # noqa

# from .clock import monitor_run  # noqa
# from .debug import print_factory  # noqa; noqa
# from .debug import File_Writer, Printer, arguments,  status, unbuffered_file  # noqa
# from .dquery import *  # noqa
# from .persistance import *  # noqa
# from .printing import *  # noqa
# from .progress import *  # noqa
# from .viewer import view, view_model  # noqa

# debug_print_filename = os.environ.get("DEBUG_LOG_FILE")
# debug_print_file = unbuffered_file(debug_print_filename)


# print to debug file
# fprint = print_factory(debug_print_file)
# fprint('-' * 30 + '\n' * 5)

# ic_config = {"prefix": ""}
# ic.configureOutput(**ic_config)
#
#
# def ic_log_to_file():
# ic_config.update({"outputFunction": debug_print_file.write})
# ic.configureOutput(**ic_config)


# a printer with indentation
# p = Printer()
