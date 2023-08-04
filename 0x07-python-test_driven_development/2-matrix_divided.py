#!/usr/bin/python3
"""Module for dividing matrices.

The module has one fucntion "matrix_divided"
The function takes a matrix and a number to divide by.

The matrix should include only numbers.
"""


def matrix_divided(matrix, div):
    """Function for dividing a matrix

    Args:
        matrix(list of lists): only contains int,float
        div(int, float): divisor

    Returns:
        A new divided matrix.
    """
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == []:
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return []
    if type(matrix) != list:
        raise TypeError(m)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(m)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(m)
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda x: list(map(lambda i: round(i/div, 2), x)), matrix))
