#!/usr/bin/python3
"""
Module containing a subclass named 'MyList' inheriting 
from the 'list' class.
"""


class MyList(list):
    """
    Class derived from the 'list' class.
    """

    def print_sorted(self):
        """
        Function that displays a list in ascending order.
        """
        print(sorted(self))