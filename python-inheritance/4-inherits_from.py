#!/usr/bin/python3
"""
Module containing the 'inherits_from' function.
"""


def inherits_from(obj, a_class):
    """
    Function that checks if an object is an instance of a
    class that inherits from the specified class.

    Args:
        obj: The object to evaluate.
        class_name: The specified class.

    Returns:
    True if obj is an instance of a class inherited
    from class_name, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
