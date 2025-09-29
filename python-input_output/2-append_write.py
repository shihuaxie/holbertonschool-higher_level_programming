#!/usr/bin/python3
"""
Module: 2-append_write
Function: append_write
write a function that appends a string
at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a file
    Returns the number of chars added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
