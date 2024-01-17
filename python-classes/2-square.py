#!/usr/bin/python3

"""Defines a class named square"""


class Square:
    """Names and represents square"""

    def __init__(self, size=0):
        """Initializes new square

        Args:
            size (int): the size of new square 
            (private instance attribute)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
