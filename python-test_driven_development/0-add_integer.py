#!/usr/bin/python3
"""Module that defines a function that adds two integers."""

def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    Floats are casted to integers.
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
