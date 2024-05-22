#!/usr/bin/python3
"""
The module checks whether an object is an
instance or a subclass of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to determine if an object is an instance
    of or inherits from the specified class.

    Args:
        obj: The object to evaluate.
        a_class: The specified class.

    Returns:
        True if obj is an instance of a_class or its
        subclass, otherwise False.
    """
    return isinstance(obj, a_class)
