#!/usr/bin/python3
"""
Module for printing a square

This module provides a function to print a square of given size using #.
"""


def print_square(size):
    """
    Print a square with the character #
    
    Args:
        size: Size length of the square (must be an integer >= 0)
    
    Returns:
        None (prints to stdout)
    
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    
    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(1)
        #
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square
    for i in range(size):
        print("#" * size)
