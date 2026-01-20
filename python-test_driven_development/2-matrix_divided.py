#!/usr/bin/python3
"""
Module for matrix division

This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number
    
    Args:
        matrix: List of lists of integers or floats
        div: Number to divide by (integer or float)
    
    Returns:
        New matrix with divided elements rounded to 2 decimal places
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """
    
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if matrix is not empty and is list of lists
    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if matrix has at least one row with elements
    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check row size consistency
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Divide and round to 2 decimal places
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
