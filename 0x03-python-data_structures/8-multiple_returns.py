#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string"""
    return (len(sentence), sentence[0]) if len(sentence) else (0, None)
