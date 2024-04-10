#!/usr/bin/python3
""" This module divides a matrix. """


def matrix_divided(matrix, div):
    """ This function divides a matrix.
    parameter: matrix: contains a list of lists.
        div: divides a matrix, cannot be zero.
    Return: a new matrix.
    Raises: typeerror and zerodivision error.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(ele, (int, float))
                for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
