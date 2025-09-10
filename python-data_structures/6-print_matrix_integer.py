#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # if is not the last element, then add a space
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                # The last ele shoudn't have any space
                print("{:d}".format(row[i]), end="")
        print()  # new line
    