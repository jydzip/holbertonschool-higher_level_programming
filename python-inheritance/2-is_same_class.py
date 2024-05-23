#!/usr/bin/python3
"""
    Function file for is_same_class.
"""


def is_same_class(obj, a_class):
    """
        Check if object if exactly an instance of the specified class.

        Arguments:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    if isinstance(obj, a_class):
        _dir_obj = dir(obj)
        _dir_class = dir(a_class)
        for dd in _dir_obj:
            if dd not in _dir_class:
                return False
        return True
    return False
