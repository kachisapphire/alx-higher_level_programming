#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        square.append([x**2 for x in row])
    return square
