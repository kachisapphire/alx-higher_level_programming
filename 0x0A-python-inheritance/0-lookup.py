#!/usr/bin/python3
""" Thi module returns a list of module and attribute. """


def lookup(obj):
    """ This function returns all modules and
    attribute of obj.
    """
    return (dir(obj))
