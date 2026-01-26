#!/usr/bin/python3
"""
2-is_same_class module
Defines a function that returns True if the object is exactly
an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: The object to test.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
