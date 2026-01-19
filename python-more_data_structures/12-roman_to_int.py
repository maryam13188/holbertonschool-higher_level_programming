#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, prev = 0, 0
    for char in reversed(roman_string):
        value = roman.get(char, 0)
        if not value:
            return 0
        total += -value if value < prev else value
        prev = value
    return total
