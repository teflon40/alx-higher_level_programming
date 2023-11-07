#!/usr/bin/python3
""" a module containing a lookup function"""


def lookup(obj):
    """ list of available attributes and methods of an object """
    return list(dir(obj))
