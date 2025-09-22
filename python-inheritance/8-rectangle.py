#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""
# import BaseGeometry from the previous task module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle defined by private width and height, validated by BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated positive integers.

        Args:
            width (int): rectangle width (> 0)
            height (int): rectangle height (> 0)
        """
        # validate width&height-integer_validator(self, name, value)
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        # then assign to private attributes
        self.__width = width
        self.__height = height
