#!/usr/bin/python3
"""
A function that validate if the onject is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False."""
    # type(obj) is a_class is a boolean expression
    return type(obj) is a_class
