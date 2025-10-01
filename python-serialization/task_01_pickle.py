#!/usr/bin/python3
"""Serialize and deserialize custom Python objects using the pickle module."""

import pickle


class CustomObject:
    """a custom Python class named CustomObject"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return an instance."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None
