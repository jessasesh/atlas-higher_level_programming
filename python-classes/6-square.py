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

    @property
    def position(self):
        """ Retrieves position of the square """
        return self.__position

    @position.setter
    def position(self, value):

        # Check if value is a tuple of 2 positive integers
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check of elements are integers
        if not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check if both integers are positive
        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        # Sets the position to new value
        self.__position = value

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
