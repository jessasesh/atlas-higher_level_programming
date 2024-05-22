#!/usr/bin/python3
"""
Import.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class definition of square - subclass of rectangle.
    """

    def __init__(self, size):
        """
        Method that initializes square instance.

        Args:
            size : size of a side of the square
        """
        self.integer_validator("size", size)
        #  validate and set size of square
        super().__init__(size, size)  # size is both width and height
        self.__size = size

    def area(self):
        """
        Figures area.

        Returns:
            area
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns string representation of square.

        Return:
            square (str representation)
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
