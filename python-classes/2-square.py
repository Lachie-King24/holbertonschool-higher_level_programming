#!/usr/bin/python3
"""Define a square"""


class Square:
    """Define a square"""
    def __init__(self, __size):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
