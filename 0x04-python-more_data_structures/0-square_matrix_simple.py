#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in a matrix"""
    new_matrix = []
    for my_list in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, my_list)))
    return new_matrix
