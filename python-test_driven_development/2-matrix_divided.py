#!/usr/bin/python3
"""
This module contains the matrix_divided function
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    row_length = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)

        for element in row:
            if not isinstance(element, (int, float)):
                msg = "matrix must be a matrix (list of lists) of integers/floats"
                raise TypeError(msg)

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            rounded = round(result, 2)
            if rounded == -0.0:
                rounded = 0.0
            new_row.append(rounded)
        new_matrix.append(new_row)

    return new_matrix
