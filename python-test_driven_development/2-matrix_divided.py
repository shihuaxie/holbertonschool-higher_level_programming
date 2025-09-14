#!/usr/bin/python3
"""Divide all elements of a matrix by a number."""

def _is_num(x):
    """Return True if x is an int or float (bool counts as int per Python)."""
    return isinstance(x, (int, float))


def _is_bad_float(x):
    """Return True if x is NaN or +/-Infinity (no imports)."""
    return isinstance(x, float) and (x != x or x in (float('inf'), -float('inf')))


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by `div`.

    Rules
    -----
    - `matrix` must be a list of lists of integers/floats, otherwise:
      TypeError("matrix must be a matrix (list of lists) of integers/floats")
    - Each row must have the same size, otherwise:
      TypeError("Each row of the matrix must have the same size")
    - `div` must be a number (int or float), otherwise:
      TypeError("div must be a number")
    - If `div` == 0, raise:
      ZeroDivisionError("division by zero")
    - Result elements are rounded to 2 decimal places.
    - Original matrix is not modified.
    """
    # Validate matrix
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix) or
            any(not _is_num(n) for row in matrix for n in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not _is_num(div) or _is_bad_float(div):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Compute new matrix
    return [[round(n / div, 2) for n in row] for row in matrix]
