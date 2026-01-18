#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace element in list at specific position."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
