#!/usr/bin/python3
"""Defines a BaseGeometry class with an area method"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")
