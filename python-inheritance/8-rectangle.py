#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry"""

Rectangle = __import__('7-base_geometry').BaseGeometry

class Rectangle(Rectangle):
    """Represents a rectangle with private width and height"""

    def __init__(self, width, height):
        """Initialize a new Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
