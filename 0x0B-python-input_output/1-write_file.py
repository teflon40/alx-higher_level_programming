#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Args:
        filename (str): name of file
        text (str): contents to be written
    Return:
        the number of characters written
    """
    with open(filename, "w") as file_object:
        return file_object.write(text)
