#!/usr/bin/python3
"""Module 0-add_integer: adds two integers."""


def add_integer(a, b=98):
    """Returns the sum of a and b as integers.

    a and b must be integers or floats; floats are cast to int.
    Raises TypeError if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
