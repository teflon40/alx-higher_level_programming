#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    for sub_list in matrix:
        for num in sub_list:
            print("{:d}".format(num), end="" if num is sub_list[-1] else " ")
        print("")
