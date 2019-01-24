import logging
from collections import namedtuple
from inspect import ismodule

from sqlalchemy import inspect

Attribute_Group = namedtuple('Attribute_Group', ['attributes', 'name'])


def doc_header(o):
    try:
        return o.__doc__.split('\n')[0]
    except (AttributeError):
        return None


class Object_Viewer:
    def __init__(self, o, printer=print):
        self.o = o
        self.print = printer

    def view(self):
        self.print_title()
        attributes = self.get_attributes_names()
        self.set_column_width(attributes)
        groups = self.group_attributes(attributes)
        for group in groups:
            self.view_group(group)

    def get_attributes_names(self):
        return [a for a in dir(self.o) if self.is_viewed(a)]

    def get_attribute(self, a):
        try:
            return getattr(self.o, a)
        except (TypeError, AttributeError, ValueError):
            return None

    def group_attributes(self, attributes):
        """split attributes into groups"""

        callables = Attribute_Group(attributes=[], name='callables')
        properties = Attribute_Group(attributes=[], name='properties')
        modules = Attribute_Group(attributes=[], name='modules')
        for a in attributes:
            value = self.get_attribute(a)
            if callable(value):
                callables.attributes.append(a)
            elif ismodule(value):
                modules.attributes.append(a)
            else:
                properties.attributes.append(a)
        return [modules, properties, callables]

    def view_group(self, group):
        if not group.attributes:
            return
        self.print_group_title(group)
        for a in group.attributes:
            self.print_attribute(a)

    def is_viewed(self, a):
        return not a[0] == '_'

    # -------------------printers-----------------------

    def set_column_width(self, attributes):
        self.first_column_width = max([len(name) for name in attributes])

    def print_title(self):
        self.print(f'type : {type(self.o)}')

    def print_group_title(self, group):
        if group.name:
            self.print(f'\n---| {group.name}\n')

    def print_attribute(self, a):
        attr = self.get_attribute(a)
        if attr is None:
            print(f'{a:{self.first_column_width}} : ...')
            return
        if callable(attr):
            formatted = f'{a}()'
            self.print(f'{formatted:{self.first_column_width}} : {doc_header(attr)}')
        else:
            type_ = type(attr)
            base_types = [int, bool, type(None), dict, frozenset, str, list, tuple]
            if type_ in base_types:
                type_info = ''
            else:
                type_info = type_
            attr_str = str(attr)
            if len(attr_str) > 40:
                attr_str = f'{attr_str[:20]}...      ({len(attr_str)})'
            self.print(f'{a:{self.first_column_width}} : {attr_str} {type_info}')


def format_logger(l):
    info = []
    info.append(f'logger : {l.name}({logging.getLevelName(l.level)})')
    if l.propagate:
        info.append(f'propagate to : {l.parent!r}')
    else:
        info.append('no propagation')
    for handler in l.handlers:
        info.append(f'handler : {handler.__class__.__name__}')
    return '\n'.join(info)


def view_model(model):
    mapper = inspect(model)
    print(mapper.class_)
    print()
    print('---| relationships')
    for r in mapper.relationships.keys():
        print(r)
    print()
    print('---| properties')
    for p in mapper.column_attrs:
        print(f'{p.key}')


# -----------------------------------------------


def view(o, **kwargs):
    if isinstance(o, logging.Logger):
        print(format_logger(o))
    else:
        viewer = Object_Viewer(o, **kwargs)
        viewer.view()
