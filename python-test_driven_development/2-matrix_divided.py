#!/usr/bin/python3
"""Module that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals."""
    
    # Check div type
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Check matrix type and row sizes
    if (type(matrix) is not list or
        any(type(row) is not list for row in matrix) or
        len(matrix) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_len = len(matrix[0])
    new_matrix = []
    
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    
    return new_matrix
