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

    def __str__(self):
        """override str representation"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes with values"""
        if args:
            args_len = len(args)
            self.id = args[0]
            self.size = args[1] if args_len > 1 else self.size
            self.x = args[2] if args_len > 2 else self.x
            self.y = args[3] if args_len > 3 else self.y
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
