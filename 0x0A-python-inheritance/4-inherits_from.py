#!/usr/bin/python3
""" module that checks for derived class"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    return True if issubclass(type(obj), a_class)\
        and type(obj) != a_class else False
