#!/usr/bin/python3
"""
Module for matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices
    
    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)
    
    Returns:
        Result matrix after multiplication
    
    Raises:
        TypeError: For various type-related errors
        ValueError: For empty matrices or incompatible dimensions
    """
    # Validate m_a
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    
    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    
    # Validate m_b  
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Check elements are integers or floats
    for row in m_a:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    
    for row in m_b:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    
    # Check rectangular shape
    a_cols = len(m_a[0])
    for row in m_a:
        if len(row) != a_cols:
            raise TypeError("each row of m_a must be of the same size")
    
    b_cols = len(m_b[0])
    for row in m_b:
        if len(row) != b_cols:
            raise TypeError("each row of m_b must be of the same size")
    
    # Check multiplication compatibility
    if a_cols != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(b_cols):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            row_result.append(sum_val)
        result.append(row_result)
    
    return result
