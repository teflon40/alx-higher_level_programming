#!/usr/bin/python3
""" module that defines a Geometry """


class BaseGeometry:
    """ defines a class Geometry """

    def area(self):
        """ raises an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
