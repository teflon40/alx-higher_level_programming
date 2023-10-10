#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list"""
    if not (idx >= len(my_list) or idx < 0):
        del my_list[idx]
    return my_list
