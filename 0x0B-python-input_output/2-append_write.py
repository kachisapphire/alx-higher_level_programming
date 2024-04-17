#!/usr/bin/python3
""" This module appends to a file. """


def append_write(filename="", text=""):
    """ this function ppends a string at the end of a text file (UTF8)
    eturns the number of characters added. """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
