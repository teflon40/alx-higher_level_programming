#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds and returns the biggest integer of a list"""
    return None if my_list == [] else sorted(my_list)[-1]
