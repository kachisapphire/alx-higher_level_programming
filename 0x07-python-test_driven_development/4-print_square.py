#!/usr/bin/python3
""" This module prints a square. """


def print_square(size):
    """ This function prints a square with the character #.
    parameter: size(the length of the square)
    raises: typereeror is size is not an integer.
        valuerror if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            [print('#', end="") for j in range(size)]
            print("")
