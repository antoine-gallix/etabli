"""Utils for creating unix filter programs
"""

import fileinput
import re


def print_line(line):
    print(line, end='')


def print_numbered_line(line):
    print(f'{fileinput.lineno():4} {line}', end='')


def apply_to_lines(process_function):
    with fileinput.input() as f:
        for line in f:
            process_function(line)


def strip_ack_output(line):
    ack_output_pattern = '(.*):(.*):.*'
    match = re.match(ack_output_pattern, line)
    if match:
        print(f'{match.group(1)}\t{match.group(2)}')
