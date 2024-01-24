#!/usr/bin/python3
"""
This is a function that returns True/False
based on if the object is an exact instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    This checks if an object is a match.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        If object is exactly an 
        instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
