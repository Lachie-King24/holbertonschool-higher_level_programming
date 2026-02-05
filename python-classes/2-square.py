#!/usr/bin/python3
"""Define a square"""


class Square:
    """Define a square"""
    def __init__(self, size=0)
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
