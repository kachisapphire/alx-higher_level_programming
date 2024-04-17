#!/usr/bin/python3
""" This module contains a calass and its subclass. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A subclass which inherits from Rectangle. """
    def __init__(self, size):
        """ Instantiation of square. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

