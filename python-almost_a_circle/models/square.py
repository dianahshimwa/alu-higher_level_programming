#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate.
            y (int): Y coordinate.
            id (int): ID.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        self.validate_integer("width", value, greater_than_zero=True)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        self.validate_integer("height", value, greater_than_zero=True)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x with validation."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y with validation."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, greater_than_zero=False):
        """Validates that a value is an integer and positive when required.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.
            greater_than_zero (bool): Whether value must be > 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if greater_than_zero:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Display the Rectangle using '#'."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update attributes using *args or **kwargs."""
        if args and len(args) > 0:
            attr_order = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attr_order, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
