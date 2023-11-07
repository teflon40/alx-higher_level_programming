#!/usr/bin/python3
""" a module containing a derived class of Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a square, subclass of Rectangle """

    def __init__(self, size):
        """ instantiation of instance attributes"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of a square """
        return self.__size * self.__size
