#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""
# import BaseGeometry from the previous task module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with validated private size."""

    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            size (int): the size of the square (> 0)
        """
        # size must be a positive int
        Rectangle.integer_validator(self, "size", size)
        # store private size
        self.__size = size
        # use super() to use __int__ from parent class Rectangle
        super().__init__(size, size)

    def __str__(self):
        """Return printable representation: [Square] <size>/<size>."""
        return f"[Square] {self.__size}/{self.__size}"
