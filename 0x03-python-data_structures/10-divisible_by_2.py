#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    new_list = list(True if not num % 2 else False for num in my_list)
    return new_list
