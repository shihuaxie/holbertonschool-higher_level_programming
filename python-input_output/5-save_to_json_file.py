#!/usr/bin/python3
"""
Module that saves an object to a file in JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: Any JSON-serializable Python object.
        filename (str): Path to the output file.
    """
    # Open the file in write mode
    # then use json.dump() to write the object as JSON
    with open(filename, "w",  encoding="utf-8") as f:
        json.dump(my_obj, f)
