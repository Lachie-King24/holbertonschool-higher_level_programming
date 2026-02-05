#!/usr/bin/python3
"""Define a Square with a Class"""


class Square:
    """Define a Square"""
    def __init__(self, size=0):
        self.size = size

    #getter for size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
