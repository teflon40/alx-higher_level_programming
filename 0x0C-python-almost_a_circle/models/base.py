#!/usr/bin/python3
"""class Base module"""
import json


class Base:
    """class for base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string reprentation of object"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
