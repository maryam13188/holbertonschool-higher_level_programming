#!/usr/bin/python3
"""
3-is_kind_of_class module
Defines a function that returns True if the object is an instance
of, or inherits from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to test.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is instance of a_class or subclass, else False.
    """
    return isinstance(obj, a_class)
