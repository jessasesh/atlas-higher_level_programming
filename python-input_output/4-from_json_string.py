#!/usr/bin/python3
"""
This function that returns an object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
