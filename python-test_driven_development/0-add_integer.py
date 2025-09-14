#!/usr/bin/python3
"""Module for adding two integers.
This module exposes a single function `add_integer(a, b=98)` that returns
the integer addition of `a` and `b`. Arguments may be ints or floats;
floats are cast to ints before addition. Otherwise a `TypeError` is raised.
"""


def _is_bad_float(x):
    """Return True if x is NaN or Infinity (no imports used)."""
    # NaN is the only float that is not equal to itself
    if x != x:
        return True
    # Detect +/-Infinity using float('inf') sentinels
    inf = float('inf')
    return x == inf or x == -inf

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
    if not isinstance(a, (int, float)) or (isinstance(a, float) and _is_bad_float(a)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or (isinstance(b, float) and _is_bad_float(b)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
