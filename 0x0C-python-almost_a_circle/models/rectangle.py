#!/usr/bin/python3
"""class for rectangle"""
from models.base import Base


class Rectangle(Base):
    """Model a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
