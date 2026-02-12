#!/usr/bin/python3
"""Module that defines MyList, a subclass of list with a print_sorted method"""


class MyList(list):
    """Subclass of list with a method to print sorted list"""

    def print_sorted(self):
        print(sorted(self))
