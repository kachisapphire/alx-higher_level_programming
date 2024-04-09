#!/usr/bin/python3
""" This module prints a user's input. """


def say_my_name(first_name, last_name=""):
    """ This function prints the above parameter based
    on users input.
    Raises a typeerror if input is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
