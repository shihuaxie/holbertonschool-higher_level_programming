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

        # self.__position = position is incorrect
        # bcz position & size  must be validated by setter
        self.size = size
        self.position = position

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
        if (not isinstance(value, tuple) or
                # case: there should be 2 ele in tuple.
                len(value) != 2 or
                # case: every ele in the tuple must be an int.
                not all(isinstance(num, int) for num in value) or
                # case: every ele in the tuple must be positive int.
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        Prints in stdout the square with the character '#'

        If size is 0, prints an empty line.

        Position is used to set the horizontal and vertical offsite.
        """
        if self.__size == 0:
            print("")    # empty line
            return
        # Example: Square(3, (1, 2))
        # vertical: position[1] = 2 horizontal: position[0] = 1
        # Vertical offset (position[1]) print empty line before square
        for _ in range(self.__position[1]):
            print("")

        # Each line of the square
        for _ in range(self.__size):
            # Horizontal offset  (position[0]) print tabs before each row
            print(" " * self.__position[0] + "#" * self.__size)
