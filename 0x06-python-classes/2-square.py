#!/usr/bin/python3
"""Write a class Square a class by size"""


class Square:
    """Defines a class Square"""

    def __init__(self, size=0):
        """
            Initialize size attribute
            Args:
                size
            Errors:
                TypeError
                ValueError
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
