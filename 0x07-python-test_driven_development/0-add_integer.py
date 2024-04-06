#!/usr/bin/python3
""" This is a module that adds two integers."""


def add_integer(a, b=98):
    """ this function adds two integers.
        parameters: a and b.
        Returns: the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
