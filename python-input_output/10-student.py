#!/usr/bin/python3
"""Module defining a Student class."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # public method
    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attribute names in this list
        are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            # create an empty dict - result
            result = {}
            # loop all attrs in the list
            for i in attrs:
                # if the attr is contained in the list, then put in dict
                if hasattr(self, i):
                    result[i] = getattr(self, i)
            return result
        else:
            return self.__dict__
