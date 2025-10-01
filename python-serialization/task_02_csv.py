#!/usr/bin/python3
"""This module is Converting CSV Data to JSON Format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and save it as data.json.
    Returns True if successful, False otherwise.
    """
    # 1: reading the CSV data
    # 2: converting each row into a dictionary
    # 3: writing these dictionaries as a JSON array to a file

    try:
        data = []
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
