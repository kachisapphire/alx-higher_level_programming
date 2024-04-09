#!/usr/bin/python3
""" this module contains a class lockedclass. """


class LockedClass:
    """ This is a class with no attribute.
    slots restricts creation of dynamic attributes.
    """
    __slots__ = ["first_name"]
