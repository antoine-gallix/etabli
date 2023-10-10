import click
import rich

import etabli.persistance


@click.command
@click.argument("file")
def print_variable_file(file):
    rich.print(etabli.persistance.load_pickle(file))
