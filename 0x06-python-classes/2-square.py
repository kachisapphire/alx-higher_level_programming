#!/usr/bin/python3
""" This module contains a class.
"""


class Square:
    """ This is a class Square.
    It is made up of attributes and instances.
    """
    def __init__(self, size=0):
        """ This is a documentation for the function.
        Parameter:
            size: initialised to zero.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
