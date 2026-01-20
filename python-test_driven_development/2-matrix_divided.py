#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divide matrix elements by div"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(err_msg)
    
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(err_msg)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(err_msg)
    
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = round(num / div, 2)
            if result == -0.0:
                result = 0.0
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
