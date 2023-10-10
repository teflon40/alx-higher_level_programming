#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    tup1, tup2 = (tuple_a + (0, 0), tuple_b + (0, 0))
    sum = (tup1[0] + tup2[0], tup1[1] + tup2[1])
    return sum
