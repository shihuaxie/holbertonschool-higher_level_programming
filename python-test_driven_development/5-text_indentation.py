#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Rules:
      - `text` must be a string, otherwise:
        TypeError("text must be a string")
      - After any of the separators ('.', '?', ':'), print two new lines.
      - There should be no leading spaces at the beginning of a printed line
        (skip consecutive spaces after a separator).

    This function prints directly and returns nothing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    # Skip any leading spaces at very start
    while i < n and text[i] == " ":
        i += 1

    while i < n:
        ch = text[i]
        print(ch, end="")

        if ch in ".?:":
            # Break the paragraph with two new lines
            print("\n")
            i += 1
            # Skip all following spaces so the next printed line
            # doesn't start with spaces
            while i < n and text[i] == " ":
                i += 1
            continue

        i += 1
