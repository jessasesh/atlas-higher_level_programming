#!/usr/bin/python3
""" 
Creates a class.
"""


class BaseGeometry:
    """ 
    Empty Class.
    """
    def area(self):
        """
        Incomplete method that raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the passed value

        Args:
            name : name of value (str)
            value : the value (int)

        Raises:
            TypeError : if value not integer
            ValueError : if valuee is less than or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class definition of rectangle - subclass
    """
    def __init__(self, width, height):
        """
        Method that initializes Rectangle instance

        Args:
            width : width of rectangle
            height : height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """ 
        calculates the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ 
        Returns a representation of rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
    