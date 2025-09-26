#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends list
and prints messages when items are added or removed.
"""


class VerboseList(list):
    """A list subclass that prints notifications on modification."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        """Extend the list with items and print how many were added."""
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """Remove an item from the list and print a message."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print which one was removed."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
