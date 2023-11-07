#!/usr/bin/python3
""" A module containing a derived class of int"""


class MyInt(int):
    """ Defines a derieved class of int """

    def __eq__(self, data):
        """Override == opeartor with != """
        return self.real != data

    def __ne__(self, data):
        """Override != operator with == """
        return self.real == data
