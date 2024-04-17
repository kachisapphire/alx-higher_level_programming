#!/usr/bin/python3
""" This is an empty class. """


class BaseGeometry:
    """ This class takes in a few parameters. """
    def area(self):
        """ no instruction yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this function validates value. """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
