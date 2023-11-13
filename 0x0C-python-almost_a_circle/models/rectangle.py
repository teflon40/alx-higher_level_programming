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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of the rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Prints rectangle with #"""
        for _ in range(self.__height):
            print('#'*self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " + \
                f"{self.__width}/{self.__height}"
