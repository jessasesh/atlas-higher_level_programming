#!/usr/bin/python3
    """
    This is a function that returns the
    list of available attributes and
    methods of an object.
    """


def lookup(obj):
    """
    Returns a list of attributes available
    for a given object.
    
    Args:
        obj: The object for which attributes
             need to be looked up.
    Returns:
        A list containing the names of
        available attributes for object.
    """
    return (dir(obj))
