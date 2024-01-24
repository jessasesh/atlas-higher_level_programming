#!/usr/bin/python3
"""
This function checks if an object is an
inherited instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Checks for inheritance.

    Returns:
        If object is an inherited instance
        of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class) and obj.__class__ != a_class:
        return True
    else:
        return False
