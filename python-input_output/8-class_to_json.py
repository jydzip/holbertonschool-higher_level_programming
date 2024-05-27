#!/usr/bin/python3
"""
    File function for class_to_json().
"""
import json


def class_to_json(obj):
    """
        Returns the dict description with simple data structure of an object.
        Arguments:
            obj: Object to list.
    """
    _str = json.dumps(obj, default=lambda o: o.__dict__)
    return json.loads(_str)
