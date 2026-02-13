#!/usr/bin/python3
"""Define Shape abstract class and its Circle and Rectangle subclasses"""


from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    """Abstract base class for all shapes"""

    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


# Circle class
class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class
class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Duck typing function
def shape_info(shape):
    """Print the area and perimeter of any shape"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
