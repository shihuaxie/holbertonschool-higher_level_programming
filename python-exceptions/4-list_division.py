#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    result = []

    for i in range(list_length):
        value = 0  #  Default result for each position

        try:
            # Try to divide the elements at index i
            value = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            # Division by zero case
            print("division by 0")

        except TypeError:
            # If one of the elements is not an int/float
            print("wrong type")

        except IndexError:
            # If either list is shorter than list_length
            print("out of range")

        finally:
            # Append result for this index
            # If an exception occurred, value stays as 0
            result.append(value)

    return result
