import click
import rich

import etabli.persistance

main = click.Group()


@main.command
@click.argument("file")
def print_variable_file(file):
    rich.print(etabli.persistance.load_pickle(file))


@main.command
def explore_variable_file():
    import os

    os.execvp("ipython", ["ipython", "-i", "-m", "etabli.explore"])


@main.command
def replay_call():
    import os

    os.execvp("ipython", ["ipython", "-i", "-m", "etabli.replay"])
