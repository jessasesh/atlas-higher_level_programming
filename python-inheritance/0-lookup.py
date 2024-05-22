#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods
    of the given object.
    """
    return dir(obj)
