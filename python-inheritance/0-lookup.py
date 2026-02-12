#!/usr/bin/python3
"""Define function to list attributes and methods"""


def lookup(obj):
    """Return list of available attributes and methods of object"""
    return dir(obj)
