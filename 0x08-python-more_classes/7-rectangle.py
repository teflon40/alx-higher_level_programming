#!/usr/bin/python3
"""
    Module for a class Rectangle
"""


class Rectangle:
    """
    defines a rectangle
    Args:
        width - (int): width attribute of the rectangle
        height - (int): height attribute of the rectangle
    Raises:
      TypeError: if width is not an integer
      TypeError: if height is not an integer
      ValueError if height is less than 0
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ defines a rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ validates and sets value for width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ validates and sets value for width """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ returns string representation of objects"""
        if not (self.__width and self.__height):
            return ""
        s = Rectangle.print_symbol
        return '\n'.join([str(s) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """ a str representation that can be used to recreate the object """
        return f"{self.__class__.__name__}{self.__width, self.__height}"

    def __del__(self):
        """ detects instance deletion and prints a message"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
