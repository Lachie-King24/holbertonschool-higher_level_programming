#!/usr/bin/python3
"""
Define a Rectangle
"""


class Rectangle:
    """
    Defines a square
    """

    # set counter for amount of instances
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # add counter when instance created
        Rectangle.number_of_instances += 1

    # getter for width
    @property
    def width(self):
        return self.__width

    # setter for width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # getter for height
    @property
    def height(self):
        return self.__height

    # setter for height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rows = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        # minus from instances when instance is deleted
        Rectangle.number_of_instances -= 1
