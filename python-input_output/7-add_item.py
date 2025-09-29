#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then saves them to a file (add_item.json)."""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # if file exist, read the list
    items = load_from_json_file(filename)
except FileNotFoundError:
    # if file not exist, create an empty list
    items = []

# add the command args（sys.argv[1:]）
items.extend(sys.argv[1:])

# save the updated list to the filename
save_to_json_file(items, filename)
