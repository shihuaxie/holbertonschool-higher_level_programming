#!/usr/bin/python3
"""Module that defines print_square function."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is < 0.
        TypeError: if size is a float and < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
