#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position"""
    new_list = my_list[:]
    if not (idx >= len(my_list) or idx < 0):
        new_list[idx] = element
    return new_list
