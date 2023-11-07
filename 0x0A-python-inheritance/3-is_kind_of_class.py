#!/usr/bin/python3
"""Module for type/instance checking"""


def is_kind_of_class(obj, a_class):
    """ checks obj is an instance of or is an instance of
        a class that inherited from a_class,
    """
    return isinstance(obj, a_class)
