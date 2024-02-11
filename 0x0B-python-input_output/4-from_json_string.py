#!/usr/bin/python3
""" This module is about JSON."""
import json


def from_json_string(my_str):
    """ This function returns an object."""
    return json.loads(my_str)
