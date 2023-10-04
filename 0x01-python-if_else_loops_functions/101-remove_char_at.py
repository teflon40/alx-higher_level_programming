#!/usr/bin/python3

def remove_char_at(str, n):
    """Removes a character from position n"""
    if n < 0 or n >= len(str):
        return str
    new_str = ""
    i = 0
    while i < len(str):
        if i != n:
            new_str += str[i]
        i += 1
    return new_str
