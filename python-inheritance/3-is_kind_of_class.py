#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a specified class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj: Any object.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is instance of a_class or subclass, else False.
    """
    if not isinstance(obj, a_class):
        return False
    return True
