#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Defines a class by size"""

    def __init__(self, size):
        """
            Initialize private instance attribute
            args:
                size
            raises:
                TypeError
                ValueError
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
