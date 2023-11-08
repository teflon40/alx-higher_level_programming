#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Defines a class by size"""

    def __init__(self, size=0):
        """
            Initialize private instance attribute
            args:
                size (int): size of square
            raises:
                TypeError
                ValueError
        """
        self.size = size

    @property
    def size(self):
        """Retrieves private instance attribute: size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with #"""
        for _ in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print("")
