#!/usr/bin/python3
"""
4-inherits_from module
Defines a function that returns True if the object is an instance
of a class that inherits from the specified class (but not the class itself).
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass (direct or indirect)
    of a_class.

    Args:
        obj: The object to test.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is instance of a subclass of a_class, else False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
