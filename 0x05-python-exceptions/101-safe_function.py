#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        Result = fct(*args)
        return Result
    except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
