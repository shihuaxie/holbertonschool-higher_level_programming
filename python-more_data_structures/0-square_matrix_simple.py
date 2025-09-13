#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # 1: initial an empty array to store new matrixs
    new_matrix = []
    # 2: loop every rows in the original array
    for row in matrix:
        # 3: store the square value of all integers in the new row
        new_row = []
        for i in row:
            new_row.append(i ** 2)
        # 4: store new rows in the new array
        new_matrix.append(new_row)
    return new_matrix
