#!/usr/bin/python3
"""use pickle to serialize and deserialize"""


# import pickle
import pickle


class CustomObject:
    """CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize with pickle"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """deserialize with pickle"""
        with open(filename, "rb") as f:
            loaded_data = pickle.load(f)

        return loaded_data
