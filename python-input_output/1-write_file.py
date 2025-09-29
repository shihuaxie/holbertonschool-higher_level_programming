#!/usr/bin/python3
"""
Module: 1-write_file
Function: write_file
Writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).
    Overwrites the file if it already exists.

    Args:
        filename (str): The file name
        text (str): The string to write

    Returns:
        int: Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
