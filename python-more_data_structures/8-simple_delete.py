#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # pop function removes and returns an element from a list
    # if key exist, delete, otherwise return None
    a_dictionary.pop(key, None)
    return a_dictionary
