#!/usr/bin/python3
"""A square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Model a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance attributes"""
        super().__init__(size, size,  x, y, id)
        self.size = size

    @property
    def size(self):
        """retrieves size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
