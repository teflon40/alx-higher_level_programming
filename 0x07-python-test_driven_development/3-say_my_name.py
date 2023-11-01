#!/usr/bin/python3
"""
    This module contains a function that prints a name

"""


def say_my_name(first_name, last_name=""):
    """ Prints the a persons first and last name
    Args:
        first_name - (string): first name of the person
        last_name - (string): the persons last name
    Raises:
        TypeError: if first or last name is not a string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')