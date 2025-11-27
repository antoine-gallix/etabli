# -------------------core----------------------------
class Sieve:
    def __init__(self, function=None, name=None):
        if function is None:
            function = lambda _: True
            name = "True"
        self._sieve = function
        if name is not None:
            self._name = name
        else:
            self._name = function.__name__
        self._is_compound = False

    def __call__(self, thing):
        return self._sieve(thing)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name})"

    @property
    def _name_in_compound(self):
        if self._is_compound:
            return f"({self._name})"
        else:
            return self._name

    @classmethod
    def _ensure_sieve(cls, func_of_sieve):
        if not isinstance(func_of_sieve, cls):
            return cls(func_of_sieve)
        else:
            return func_of_sieve

    def __and__(self, sieve):
        sieve = self._ensure_sieve(sieve)

        def intersection(x):
            return self._sieve(x) and sieve(x)

        intersection_sieve = self.__class__(
            intersection, name=f"{self._name_in_compound} & {sieve._name_in_compound}"
        )
        intersection_sieve._is_compound = True
        return intersection_sieve

    def __or__(self, sieve):
        sieve = self._ensure_sieve(sieve)

        def union(x):
            return self._sieve(x) or sieve(x)

        union_sieve = self.__class__(
            union, name=f"{self._name_in_compound} | {sieve._name_in_compound}"
        )
        union_sieve._is_compound = True
        return union_sieve

    def __neg__(self):
        def negated(x):
            return not (self._sieve(x))

        return self.__class__(negated, f"not({self._name})")


def sieve(func):
    """Decorator to change functions into sieves"""

    return Sieve(func)


# -----------------------utils------------------------


def is_instance(type_):
    """Factory of filters based on class/type"""

    def filter_(thing):
        return isinstance(thing, type_)

    return Sieve(filter_, f"is_instance({type_.__name__})")
