#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # sorted function
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
