#!/usr/bin/python3
"""Defines a BaseGeometry class with area and integer validation"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer > 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            # hello thomas
            raise ValueError(f"{name} must be greater than 0")
