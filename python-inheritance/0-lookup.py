#!/usr/bin/python3
"""
0-lookup module
Return a list of attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of obj.
    """
    return dir(obj)
