#!/usr/bin/python3
"""
This module defines a function that returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return list of attributes and methods of obj
    Args:
        obj: The object to inspect.
     Returns:
        list: A list of attribute and method names available for the object.
    """
    # built-in function dir(obj)
    return dir(obj)
