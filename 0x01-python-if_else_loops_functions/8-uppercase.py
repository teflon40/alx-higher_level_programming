#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    """Prints a string in uppercase"""
    for ch in str:
        print("{}".format(ch if not islower(ch) else chr(ord(ch)-32)), end="")
    print(end="\n")
