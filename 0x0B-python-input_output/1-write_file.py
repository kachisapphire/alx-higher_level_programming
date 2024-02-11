#!/usr/bin/python3
""" This module writes a string."""


def write_file(filename="", text=""):
    """ This function writes a string to a file.
    parameters:
        filename: file to be written to.
        text: string to write to file.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        file = my_file.write(text)
        return (file)
