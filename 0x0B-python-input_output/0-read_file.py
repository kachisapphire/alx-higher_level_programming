#!/usr/bin/python3
""" this is a module of a function thats reads a file.
"""


def read_file(filename=""):
    """ The function read_file reads a file.
    parameters:
        filename: file to be read
    """
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        file = my_file.read()
        print(file)
