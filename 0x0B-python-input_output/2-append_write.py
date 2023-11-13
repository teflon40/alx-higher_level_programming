#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    Args:
        filename (str): name of a text file
        text (str): contents to append
    Return:
        the number of characters added
    """
    with open(filename, "a") as file_object:
        return file_object.write(text)
