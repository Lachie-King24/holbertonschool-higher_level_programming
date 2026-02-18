#!/usr/bin/python3
"""Script that adds all arguments to a python list"""


# import functions
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


# name file
filename = "add_item.json"


try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
