#!/usr/bin/python3
"""
Module for adding two integers

This module provides a function to add two integers or floats.
The function handles type checking and conversion from float to integer.
"""


def add_integer(a, b=98):
    """
    Add two integers
    
    Args:
        a: First number (integer or float)
        b: Second number (integer or float), defaults to 98
    
    Returns:
        Integer sum of a and b
    
    Raises:
        TypeError: If a or b are not integers or floats
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    
    # Check if a is valid
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if b is valid
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    # Return the sum as integer
    return int(a + b)
