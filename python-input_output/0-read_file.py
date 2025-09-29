#!/usr/bin/python3
"""
Module: 0-read_file
Function: read_file
Reads a text file (UTF8) and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    Args:
        filename (str): The name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        read_content = f.read()
    # Using end="" to avoid extra newline
    print(read_content, end="")
