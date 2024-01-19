#!/usr/bin/python3


"""
Program that defines a square

"""
class Square:

    """
    Defines class named Square
    """
    # Initialize data
    def __init__(self, size=0, position=(0, 0)):

        # Checks size parameter
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        # Checks position parameter
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        # Initialize instance variables
        self.__size = size
        self.__position = position

    # Calculate area of square
    def area(self):
        area = self.__size * self.__size
        return area

    # Retrieves square size
    @property
    def size(self):
        return self.__size

    # Sets size of square
    @size.setter
    def size(self, value):

        # Check and set size
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        # Resets value to new size
        self.__size = value

    # Retrieves square postition
    @property
    def position(self):
        return self.__position

    # Sets position
    @position.setter
    def position(self, value):

        # Checks for appropriate type
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        # Resets position
        self.__position = value

    # Prints the square relative to the position
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        # Prints empty lines for vertical offset
        if self.__position[1] != 0:
            for x in range(self.__position[1]):
                print("")

        # Prints spaces and symbols to create square
        for col in range(self.__size):
            if self.__position[0] > 0:
                for space in range(self.__position[0]):
                    print(" ", end="")
            for symbol in range(self.__size):
                print("#", end="")
            print("")
