#!/usr/bin/python3

"""Defines class named square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square"""
        self.size = size

    @property
    def size(self):
        """Gets and set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square using #
        If the size is 0, prints an empty line.
        Otherwise, prints a '#' followed by a new line
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
            print("")
