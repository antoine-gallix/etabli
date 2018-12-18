"""Classes to filter dictionaries
"""

from pprint import pformat


class Filter_Equal:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __call__(self, d):
        return d[self.key] == self.value


class Filter_Keys:
    def __init__(self, keys):
        self.keys = keys

    def __call__(self, d):
        return {key: d[key] for key in self.keys}


class Query(dict):
    def filter_keys(self, keys):
        """Select a subset of items

        keys : list of keys to keep
        """
        return Query(Filter_Keys(keys)(self))

    def apply(self, func, key):
        """Apply filter to item

        func : filter function
        key : item key
        """
        obj = self.copy()
        obj[key] = list(map(func, obj[key]))
        return Query(obj)

    def filter(self, func, key):
        """Apply filter to item

        func : filter function
        key : item key
        """
        obj = self.copy()
        obj[key] = list(filter(func, obj[key]))
        return Query(obj)

    def get(self, key):
        """Get element

        key : item key
        """
        obj = self.get(key)
        return Query(obj)

    def get_path(self, path):
        """Get element

        path : list of keys
        """
        obj = self
        for key in path:
            obj = obj[key]
        return Query(obj)
