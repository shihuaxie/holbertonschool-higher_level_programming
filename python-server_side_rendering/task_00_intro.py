#!/usr/bin/python3
"""
Task 0 - Creating a Simple Templating Program
"""

import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files based on
    a template and a list of attendee dictionaries.

    Each output file is named output_X.txt, where X starts from 1.
    """

    # ---------- 1. Type (str/list) validation ----------
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if (not isinstance(attendees, list)) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # ---------- 2. Empty input ---------- 
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # The placeholders we need to operate
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # ---------- 3. Handle every attendee ----------
    for index, attendee in enumerate(attendees, start=1):
        # copy from the original template
        processed = template

        # replace the placeholder
        for key in placeholders:
            value = attendee.get(key)

            # if value is empty / None -> "N/A"
            if value is None or value == "":
                value = "N/A"

            processed = processed.replace("{" + key + "}", str(value))

        # ---------- 4. Produce output file ----------
        filename = f"output_{index}.txt"

        # if the file exists, avoid overwrite
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists, skipping.")
            continue

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(processed)
        except OSError as e:
            print(f"Error writing file {filename}: {e}")
