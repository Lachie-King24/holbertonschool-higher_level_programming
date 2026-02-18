#!/usr/bin/python3
"""define function to read a full file"""


def read_file(filename=""):
    """function to read file"""
    # open file
    with open(filename, encoding="utf-8") as f:
        # print the lines that are read (whole file)
        print(f.read(), end="")
