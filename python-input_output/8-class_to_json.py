#!/usr/bin/python3
"""function to return disc description with simple data"""


import json



def class_to_json(obj):
    """
    Return dictionary of an object's attributes that are
    serializable (list, dict, str, int, bool).
    """
    return {key: value for key, value in obj.__dict__.items()}
