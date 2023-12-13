import random


def error():
    raise Exception("a wrench in the gears")


def random_error(rate):
    if random.random() < rate:
        raise Exception("an unreliable process has crashed")


class BreakOnce:
    _error_happend = False

    def __call__(self, rate):
        if (not self._error_happend) and (random.random() < rate):
            self._error_happend = True
            raise Exception("It won't happen again, I promise")


break_once = BreakOnce()


class BreakAndStayBroken:
    _error_happend = False

    def __call__(self, rate):
        if (self._error_happend) or (random.random() < rate):
            self._error_happend = True
            raise Exception("That thing is dead")


break_and_stay_broken = BreakAndStayBroken()
