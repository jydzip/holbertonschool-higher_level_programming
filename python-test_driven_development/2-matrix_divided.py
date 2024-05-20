#!/usr/bin/python3
"""
    File function for matrix_divided.
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix.
        Arguments:
            matrix (list[int | float]): List of elements matrix.
            div (int): Divider of each element.
        Return:
            (list[int | float]): New matrix list.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of "
            "integers/floats"
        )

    new_matrix = []
    if matrix:
        _len_row = len(matrix[0])

        for row in matrix:
            if len(row) != _len_row:
                raise TypeError(
                        "Each row of the matrix"
                        "must have the same size"
                )

            _new_row = []
            _len_row = len(row)

            for column in row:
                if not isinstance(column, (int, float)):
                    raise TypeError(
                            "matrix must be a matrix (list of lists) of "
                            "integers/floats"
                    )

                _new_row.append(round(column / div, 2))
            new_matrix.append(_new_row)
    return new_matrix
