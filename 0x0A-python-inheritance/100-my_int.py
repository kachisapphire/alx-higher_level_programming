#!/usr/bin/python3
""" This module contains a class int. """


class MyInt(int):
    """ This subclass inherits from int.
    MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, value):
        """ This function reverses the function 'eq'. """
        return self.real != value

    def __ne__(self, value):
        """ This function reverses 'eq'. """
        return self.real == value
