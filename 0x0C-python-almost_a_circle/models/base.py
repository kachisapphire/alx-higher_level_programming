#!/usr/bin/python3
""" This module is all about base
"""


class Base:
    """ This is a class which takes in
    the parameter id and instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the instatiator the base.
        parameter:
            id: identity of base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
