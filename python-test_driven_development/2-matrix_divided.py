#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divide matrix elements by div"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check matrix is valid
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(err_msg)
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)
    
    if not all(row for row in matrix):
        raise TypeError(err_msg)
    
    # Check all elements are numbers
    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError(err_msg)
    
    # Check all rows have same size
    first_len = len(matrix[0])
    if not all(len(row) == first_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check div is valid
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform division and rounding
    result_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            rounded = round(num / div, 2)
            # Handle -0.0 case
            if rounded == -0.0:
                rounded = 0.0
            new_row.append(rounded)
        result_matrix.append(new_row)
    
    return result_matrix
