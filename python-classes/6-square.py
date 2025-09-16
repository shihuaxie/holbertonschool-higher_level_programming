#!/usr/bin/python3
""" Module for class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the suqare (default is (0, 0))

        Raises:
            TypeError:
                If size is not an integer.
                If position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """

        if (not isinstance(size, (int))):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    # area is an instance method
    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")    # empty line
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

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

    @property
    def position(self):
        """ Get the position of the square. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square. """
        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
