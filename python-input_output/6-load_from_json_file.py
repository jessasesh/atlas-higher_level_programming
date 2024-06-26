#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object.
    """
    with open(filename) as f:
        return json.load(f)
