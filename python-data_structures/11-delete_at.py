#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete item at specific position."""
    if 0 <= idx < len(my_list):
        return my_list[:idx] + my_list[idx+1:]
    return my_list
