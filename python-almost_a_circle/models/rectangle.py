#!/usr/bin/python3
"""
Write class that inherits from another class.
"""


from models.base import Base


class Rectangle(Base):
    """
    Initializes new subclass of Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instances.

        Args:
            width
            height
            x
            y
            id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets and returns the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets and returns x-coordinate of rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets and returns the y-coordinate of rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns area of Rectangle.
        """
        return self.height * self.width

    def display(self):
        """
        Prints visual representation.
        """
        for row in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Returns string representation.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self/height}"
