#!/usr/bin/python3
"""
Write a class that inherits from another class.
"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """
    Creates subclass of Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Private instances.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns string representation.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
