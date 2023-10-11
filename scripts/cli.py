import click
import etabli.persistance
import IPython
import rich

main = click.Group()


@main.command
@click.argument("file")
def print_variable_file(file):
    rich.print(etabli.persistance.load_pickle(file))


@main.command
@click.argument("file")
def explore_variable_file(file):
    import os

    command = [
        "import etabli.persistance",
        f"var = etabli.persistance.load_pickle('{file}')",
        "print(var)",
    ]
    os.execvp("ipython", ["ipython", "-i", "-c", ";".join(command)])
