#!/usr/bin/python3
"""
This is a function that returns True/False
based upon the instance checker.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance
       or inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to compare.
    Returns:
        If object is an instance or inherited
        instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
