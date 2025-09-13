#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if input is a valid string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Mapping of Roman numerals to integer values
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    # Iterate through the Roman numeral string
    for i in range(length):
        value = roman_dict.get(roman_string[i], 0)

        # If the current value is smaller than the next one,
        # this means we need to subtract it (e.g., IV = 4)
        if i + 1 < length and value < roman_dict.get(roman_string[i + 1], 0):
            total -= value
        else:
            # Otherwise, just add the value
            total += value

    # Return the final integer result
    return total
