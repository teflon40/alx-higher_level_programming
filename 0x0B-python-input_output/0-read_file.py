#!/usr/bin/python3
""" Read a text file """


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): name of file
    """
    with open(filename) as file_object:
        content = file_object.read()
    print(content, end='')
