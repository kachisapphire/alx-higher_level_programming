#!/usr/bin/python3
""" this is a module containing a class base. """


class Base:
    """ This class has a private attribute __nb_object.
    it takes in the parameter id.
    it is the base of all the other projects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This si the instantiator for class Base. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
