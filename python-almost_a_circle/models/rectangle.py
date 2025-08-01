#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle using '#' characters."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args):
        """Assigns arguments to attributes in order:
        id, width, height, x, y
        """
        attrs = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)
