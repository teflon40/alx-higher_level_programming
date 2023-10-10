#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list like in C"""
    if idx >= len(my_list) or idx < 0:
        return None
    return my_list[idx]
