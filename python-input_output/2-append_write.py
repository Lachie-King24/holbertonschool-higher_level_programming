#!/usr/bin/python3
"""Define function that appends a string to end of file"""


def append_write(filename="", text=""):
    """function to append string"""
    with open(filename, "a", encoding="utf-8"):
        return f.append(text)
