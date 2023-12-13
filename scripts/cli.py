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


@main.command
@click.option("--precision", "-p", type=click.Choice(("s", "ms", "us")), default="s")
def timestamp(precision):
    import arrow

    timestamp = arrow.utcnow().timestamp()
    match precision:
        case "s":
            factor = 1
        case "ms":
            factor = 10e3
        case "us":
            factor = 10e6
    print(int(timestamp * factor))


@main.command
@click.argument("timestamp")
def read_timestamp(timestamp):
    import arrow

    print(arrow.Arrow.fromtimestamp(timestamp))
