#!/usr/bin/python3
""" This module returns true if argument is exactly the same. """


def is_same_class(obj, a_class):
    """ This function function that returns True if the object
    is exactly an instance of the specified class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
