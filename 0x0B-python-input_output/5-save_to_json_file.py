#!/usr/bin/python3
""" This module is about JSON."""
import json


def save_to_json_file(my_obj, filename):
    """ This function writes an object to a file.
    parameters:
            my_obj: object to write in json representation.
            filename: file to write to.
    """
    with open(filename, "w") as my_file:
        json.dump(my_obj, my_file)
