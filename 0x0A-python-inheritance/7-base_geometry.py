#!/usr/bin/python3
""" This is an empty class. """


class BaseGeometry:
    def area(self):
        """ no instruction yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this function validates value. """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

