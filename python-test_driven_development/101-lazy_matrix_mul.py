#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    
    Args:
        m_a: First matrix (list of lists)
        m_b: Second matrix (list of lists)
    
    Returns:
        The product of the two matrices as a NumPy array
    
    Raises:
        TypeError: If matrices are not lists of lists,
                   or if elements are not integers/floats,
                   or if matrices are not rectangular
        ValueError: If matrices cannot be multiplied
    """
    
    # Validate input types
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check if matrices are empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Validate matrix contents
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")
    
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")
    
    # Check if all rows have the same length (rectangular matrices)
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Convert to NumPy arrays and multiply
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b)
        return result
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
