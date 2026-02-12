#!/usr/bin/python3
"""Module that defines an abstract Animal class and its Dog and Cat subclasses"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method to return the animal's sound"""
        pass


class Dog(Animal):
    """Dog subclass of Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal"""

    def sound(self):
        return "Meow"
