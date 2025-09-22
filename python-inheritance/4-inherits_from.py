#!/usr/bin/python3
"""Nameless Module"""


def inherits_from(obj, a_class):
    """
    Return True if obj is instance of a subclass of a_class, else False.
    """
    # obj is a_class or a subclass - true
    # type(obj) is not a_class
    return issubclass(type(obj), a_class) and type(obj) is not a_class
