#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Defines a class by size"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize private instance attribute
        args:
            size (int, optional): size of square
            positon (:obj:`tuple`, optional)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        positionErr = "position must be a tuple of 2 positive integers"

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(positionErr)
        if not all(isinstance(element, int) for element in value):
            raise TypeError(positionErr)
        if any(element < 0 for element in value):
            raise TypeError(positionErr)

        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with #"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print('')
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
