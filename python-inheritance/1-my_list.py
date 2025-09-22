#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """A custom list class that extends the built-in list."""
    def print_sorted(self):
        """
        Method that prints the list in ascending sort order
        """
        print(sorted(self))
