#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry():
    """class BaseGeometry"""
    def area(self):
        """
        Raises an Exception to indicate that the area() method
        must be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
