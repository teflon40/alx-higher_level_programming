#!/usr/bin/python3
"""A simple class to simulate student"""


class Student:
    """class for student"""

    def __init__(self, first_name, last_name, age):
        """Initialize public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary repr"""
        if type(attrs) is not list:
            return vars(self)
        new_dict = {}

        for key, value in vars(self).items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
