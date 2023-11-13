#!/usr/bin/python3
"""Dict of an instance"""


def class_to_json(obj):
    """returns dictionary description"""
    return vars(obj)
