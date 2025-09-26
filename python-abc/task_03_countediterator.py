#!/usr/bin/env python3
"""This module defines a class named CountedIterator"""

class CountedIterator:
    """An iterator wrapper that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable, wrapping its iterator."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self as an iterator."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the current count of iterated items."""
        return self.count
