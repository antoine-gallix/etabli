import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass
class Watcher:
    """Call a function whenever files change"""

    targets: list[Path]
    callback: Callable

    def files(self):
        for target in self.targets:
            for dir_, _, files in target.walk():
                for file in files:
                    yield dir_ / file

    def mtimes(self):
        return [(str(file), file.stat().st_mtime) for file in self.files()]

    def watch(self):
        last_times = self.mtimes()
        try:
            while True:
                time.sleep(1)
                new_times = self.mtimes()
                if new_times == last_times:
                    pass
                else:
                    last_times = new_times
                    self.callback()
        except KeyboardInterrupt:
            exit()
