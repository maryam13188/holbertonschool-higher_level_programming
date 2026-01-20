#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divide matrix elements by div"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if (not isinstance(matrix, list) or not matrix or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float))
                for row in matrix for num in row)):
        raise TypeError(msg)
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[0.0 if round(num/div, 2) == -0.0 else round(num/div, 2)
             for num in row] for row in matrix]
