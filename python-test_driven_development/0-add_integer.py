#!/usr/bin/python3
"""
    Function file for add_integer.
"""


def add_integer(a, b=98):
    """
        Adds 2 integers.
        Arguments:
            a (int): Number 1
            b (int, optional): Number 2
        Return:
            (int): Resultat of addition.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
