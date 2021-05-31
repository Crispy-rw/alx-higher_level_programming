#!/usr/bin/python3
"""
matriz divided for an int or float
"""


def matrix_divided(matrix, div):
    """prints a matrix divided
    Args:
        matrix (list): matriz of int o float
        div (int or float): number to divide the matrix
    Raises:
        TypeError: matriz must be a mtriz list of lists
        ZeroDivisionError: cant divide by zero
        TypeError: div must be a number
        TypeError: rows must be lists
        TypeError: rows must have the same size
        TypeError: elements must be int o floats
    Returns:
        [list]: new matriz divided
    """
    message_list = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(message_list)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        lenrow = len(matrix[0])
        if not isinstance(row, list) or lenrow == 0:
            raise TypeError(message_list)
        if lenrow != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(message_list)

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]
    return new_matrix
