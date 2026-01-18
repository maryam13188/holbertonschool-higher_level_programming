#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for i, num in enumerate(row):
            # Print number with space if not last in row
            if i != len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
        if not row:  # Handle empty row
            print()
