#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    for members in sorted(a_dictionary.keys()):
        print(f"{members}: {a_dictionary[members]}")
