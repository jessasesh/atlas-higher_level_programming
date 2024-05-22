#!/usr/bin/python3
"""
Module containing the 'same_class' function, which checks whether
the provided object is an exact instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Function that determines whether the provided object
    is an instance of the specified class.

    Args:
        obj: The object to evaluate.
        a_class: The class type to check against.

    Returns:
    True if obj is an exact instance of a_class, otherwise False.
    """
    return type(obj) is a_class
