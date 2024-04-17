#!/usr/bin/python3
""" This module reads a file. """


def read_file(filename=""):
    """ this function that reads a text file (UTF8) and prints it to stdout. """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
