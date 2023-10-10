#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints integers in reverse order"""
    if type(my_list) is list:
        for integer in my_list[::-1]:
            print("{:d}".format(integer))
