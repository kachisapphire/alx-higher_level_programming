#!/usr/bin/python3
""" This module contains two classes. """


class MyList(list):
    """ This function contains a class MyList that 
    inherits from parent class list.
    """
    def print_sorted(self):
        print(sorted(self))
