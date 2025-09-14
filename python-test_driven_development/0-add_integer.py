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
    - Floats are truncated via ``int()`` before addition.
    - NaN and Infinity are not accepted.
    - On type violation raise exactly:
        * TypeError("a must be an integer")
        * TypeError("b must be an integer")

    Returns:
        int: the addition of `a` and `b`.
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
