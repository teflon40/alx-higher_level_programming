#!/usr/bin/python3
""" a module showcasing a simple usecase of inheritance"""


class MyList(list):
    """ defines a derived class of List. """

    def print_sorted(self):
        """ prints the list, but sorted """
        print(sorted(self))
