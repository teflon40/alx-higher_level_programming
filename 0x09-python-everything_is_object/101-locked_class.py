#!/usr/bin/python3
""" module of a locked class wiht no class or
    instace attributes
"""


class LockedClass:
    """ defines a class that prevents dynamically
        creating new instance attributes except with a specific name
    """
    __slots__ = ["first_name"]
