#!/usr/bin/python3
"""Load from a json file"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    Args:
        filename (str): a json file
    Return:
        python object
    """
    with open(filename) as file_object:
        return json.load(file_object)
