#!/usr/bin/python3
"""
Module for BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Incomplete method to raise Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates passed value.

        Args:
            name : name of value
            value : the value

        Raises:
            TypeError : if value is not integer
            ValueError : if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        