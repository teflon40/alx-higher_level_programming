#!/usr/bin/python3
"""Save object to a text using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a json representation
    Args:
        my_obj (obj): python object
        filename (str): text file
    """
    with open(filename, "w") as file_object:
        json.dump(my_obj, file_object)
