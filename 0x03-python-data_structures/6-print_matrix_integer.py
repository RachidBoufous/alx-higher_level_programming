#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print a matrix of integers
    Args:
        matrix (list, optional): matrix to print. Defaults to [[]].
    """
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" ")
        print()
    