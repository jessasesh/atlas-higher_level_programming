#!/usr/bin/python3

"""Creates a class named Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle.

        Args:
            width (int): the width of new rectangle
            height (int): the height of new rectangle
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """Prints string to give visual of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    @property
    def width(self):
        """Gets and sets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets and sets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns perimeter of Rectangle """
        if self.__width == 0 or self.__height == 0:
            return int(0)
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
