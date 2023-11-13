#!/usr/bin/python3
"""JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Serialize an object
    Args:
        my_obj (obj): object to serialize
    Return:
        JSON representation of my_obj
    """
    return json.dumps(my_obj)
