#!/usr/bin/python3
""" this module contains json. """
import json


def from_json_string(my_str):
    """ this function returns an object (Python data structure)
    represented by a JSON string. """
    return json.loads(my_str)
