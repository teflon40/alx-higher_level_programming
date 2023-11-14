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
        print('\n'*self.y, end="")
        for _ in range(self.height):
            print(' '*self.x + '#'*self.width)

    def __str__(self):
        """override str representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            arg_len = len(args)
            self.id = args[0]
            self.width = args[1] if arg_len > 1 else self.width
            self.height = args[2] if arg_len > 2 else self.height
            self.x = args[3] if arg_len > 3 else self.x
            self.y = args[4] if arg_len > 4 else self.y
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        new_dict = {}
        for attribute in ['id', 'width', 'height', 'x', 'y']:
            new_dict[attribute] = getattr(self, attribute)
        return new_dict
