#!/usr/bin/python3
"""
    Function file for inherits_from.
"""


def inherits_from(obj, a_class):
    """
        Check if object if an instance of the specified inherited class.

        Arguments:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    if isinstance(obj, a_class):
        return True
    return False
