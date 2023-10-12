#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionay with all values multiplied by 2"""
    return {key: value * 2 for key, value in a_dictionary.items()}
