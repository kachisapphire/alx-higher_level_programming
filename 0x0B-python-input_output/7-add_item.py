#!/usr/bin/python3
""" This module adds argument to a pythin file. """
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        items_to_add = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_to_add = []
    items_to_add.extend(sys.argv[1:])
    save_to_json_file(items_to_add, "add_item.json")
