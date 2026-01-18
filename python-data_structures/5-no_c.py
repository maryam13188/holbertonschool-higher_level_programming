#!/usr/bin/python3

def no_c(my_string):
    """Remove all 'c' and 'C' from string."""
    result = ""
    for char in my_string:
        if char not in "cC":
            result += char
    return result
