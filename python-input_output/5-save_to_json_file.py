#!/usr/bin/python3
"""Define a function that writes an object to a text file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """function to write object to file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
