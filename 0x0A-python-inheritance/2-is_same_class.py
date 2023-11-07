#!/usr/bin/python3
""" a module for class instance checking"""


def is_same_class(obj, a_class):
    """ True if obj is an instance of a_class, False otherwise """
    return type(obj) is a_class
