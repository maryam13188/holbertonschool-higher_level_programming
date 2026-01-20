#!/usr/bin/python3
"""
Module for printing name

This module provides a function to print a formatted name string.
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>"
    
    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string, defaults to empty string)
    
    Returns:
        None (prints to stdout)
    
    Raises:
        TypeError: If first_name or last_name are not strings
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print and remove trailing whitespace for doctest compatibility
    # لكن ابقي المسافة لـ main_1.py
    print(f"My name is {first_name} {last_name}".rstrip())
