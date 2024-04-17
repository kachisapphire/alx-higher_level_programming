#!/usr/bin/python3
""" This module writes a text. """


def write_file(filename="", text=""):
    """ This function  writes a string to a text file (UTF8)
    returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
