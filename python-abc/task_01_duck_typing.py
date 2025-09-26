#!/usr/bin/env python3
"""This is an abstract class Shape with two abcmethods"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    A class Shape

    Args:
        ABC
    Returns:
        Nothing
    """

    @abstractmethod
    def area(self):
        """Return numeric area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return numeric perimeter."""
        pass


# Concrete class Circle inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        #if radius <= 0:
            #raise ValueError("radius must be greater than 0")
        self._radius = radius

    def area(self):
        return math.pi * self._radius * self._radius

    def perimeter(self):
        # handle negative radius by using its magnitude
        return 2 * math.pi * abs(self._radius)


# Concrete class Rectangle inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        #if width <= 0:
            #raise ValueError("width must be greater than 0")
        #if height <= 0:
            #raise ValueError("height must be greater than 0")
        self._width = width
        self._height = height

    def area(self):
        area = self._width * self._height
        return area

    def perimeter(self):
        perimeter = 2 * (self._width + self._height)
        return perimeter


def shape_info(obj):
    """Duck-typed function: prints area and perimeter"""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
