#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns the addition of a and b.


    a and b must be integers or floats.


    Raises:
    TypeError: if aor b are not integers or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
