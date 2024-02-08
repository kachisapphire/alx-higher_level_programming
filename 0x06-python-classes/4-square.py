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

    @property
    def size(self):
        """ This function is a getter method for size.
        Returns:
            size of class Sqaure.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This function is the setter method for size.
        parameter:
            value: placeholder for size.
        Raises:
            TypeError or ValueError.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """ This function calculates the area of Square.
        Returns:
            area of a square.
        """
        return self.__size ** 2
