#!/usr/bin/python3
"""Module defining a Student class."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # public method
    def to_json(self):
        """Return a dictionary representation of the Student instance."""
        return self.__dict__
