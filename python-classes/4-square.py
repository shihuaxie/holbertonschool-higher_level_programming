#!/usr/bin/python3
""" Module for class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if (not isinstance(size, (int))):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    # area is an instance method
    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

    # Define a property
    @property       # Getter
    def size(self):
        """ Get the size of the square. """
        return self.__size

    @size.setter    # Setter
    def size(self, value):
        """ Set the size of the square. """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value  # store the value tp object
