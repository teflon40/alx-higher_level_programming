#!/usr/bin/python3
def magic_string():
    magic_string.idx = getattr(magic_string, 'idx', 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.idx)])
