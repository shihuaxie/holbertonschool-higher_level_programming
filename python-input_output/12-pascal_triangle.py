#!/usr/bin/python3
"""Pascal's Triangle generator."""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]     # Fist line

    for i in range(1, n):
        prev_row = triangle[-1]
        # Every row strats & ends with 1
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
