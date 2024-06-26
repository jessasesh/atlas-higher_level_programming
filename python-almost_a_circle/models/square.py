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

    @property
    def size(self):
        """
        Gets and returns width of square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Sets width of square.
        """
        self.width = size
        self. height = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")

    def update(self, *args, **kwargs):
        """
        Update attributes with either positional
        or keyword arguments.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of a square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
