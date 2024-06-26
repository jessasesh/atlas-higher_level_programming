#!/usr/bin/python3
"""
Function that returns the JSON representation
of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of a string object.
    """
    return json.dumps(my_obj)
