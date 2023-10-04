from functools import partial


def is_private(name):
    return name.startswith("_")


def is_method(thing, name):
    return callable(getattr(thing, name))


def filter_attributes(thing, private=None, method=None):
    filters = [lambda _: True]

    if private is False:
        filters.append(lambda name: not (is_private(name)))
    elif private is True:
        filters.append(lambda name: is_private(name))

    if method is True:
        filters.append(lambda name: is_method(thing, name))
    elif method is False:
        filters.append(lambda name: not (is_method(thing, name)))

    def attribute_filter(name):
        return all(f(name) for f in filters)

    return list(filter(attribute_filter, dir(thing)))


def short_doc(thing, name):
    doc = getattr(thing, name).__doc__
    if doc:
        return doc.split("\n")[0]


def mira(thing, all=False):
    print(type(thing))
    print()
    for a in filter_attributes(thing, method=True, private=False):
        print(f"{a}() : {short_doc(thing,a)}")
    print()
    for a in filter_attributes(thing, method=False, private=False):
        print(f"{a} = {getattr(thing,a)}")
    if all is False:
        return
    print()
    for a in filter_attributes(thing, method=True, private=True):
        print(f"{a}() : {short_doc(thing,a)}")
    print()
    for a in filter_attributes(thing, method=False, private=True):
        print(f"{a} = {getattr(thing,a)}")
