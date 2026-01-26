#!/usr/bin/python3
"""
0-lookup module
Defines a function that returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of names of attributes and methods of obj.
    """
    return dir(obj)
