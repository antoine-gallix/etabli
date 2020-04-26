import attr
import time


def dot():
    print(".", end="", flush=True)


@attr.s
class Counter:
    _count = attr.ib(0)
    _last_print = attr.ib(float('-inf'))
    # refresh factor
    delay = attr.ib(0.25)

    def count(self):
        self._count += 1
        t = time.perf_counter()
        if t - self._last_print > self.delay:
            self._last_print = t
            print("\r", end="")
            print(self._count, end="")
