#!/usr/bin/python3
"""Module for adding two integers.
This module exposes a single function `add_integer(a, b=98)` that returns
the integer addition of `a` and `b`. Arguments may be ints or floats;
floats are cast to ints before addition. Otherwise a `TypeError` is raised.
"""

def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Rules:
    - `a` and `b` must be integers or floats.
    - If they are floats, they are cast to ints (truncation).
    - Otherwise raise TypeError with the exact messages:
      * "a must be an integer"
      * "b must be an integer"

    Returns:
        int: the addition of `a` and `b`.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
