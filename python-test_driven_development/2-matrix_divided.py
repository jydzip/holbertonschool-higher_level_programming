#!/usr/bin/python3
"""
    File function for matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists of int or float): List of elements matrix.
        div (int or float): Divider of each element.

    Returns:
        list of lists of float: New matrix list with each element divided
        by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
        or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) "
                "of integers/floats")

    new_matrix = []
    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                    "Each row of the matrix "
                    "must have the same size")

        new_row = []

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                        "matrix must be a matrix "
                        "(list of lists) of integers/floats")

            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)
    return new_matrix
