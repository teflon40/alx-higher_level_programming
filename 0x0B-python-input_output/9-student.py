#!/usr/bin/python3
"""A simple class to simulate student"""


class Student:
    """class for student"""

    def __init__(self, first_name, last_name, age):
        """Initialize public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary repr"""
        return vars(self)
