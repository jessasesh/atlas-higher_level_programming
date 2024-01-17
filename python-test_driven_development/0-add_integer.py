#!/usr/bin/python3

"""
A function that computes the sum of 2 integers
"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as integers

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of two arguments

    Raises:
        TypeError: If either of the arguments are not integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))