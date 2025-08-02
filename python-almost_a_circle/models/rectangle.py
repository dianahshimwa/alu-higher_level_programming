#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle with validation."""
        self.validate_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle with validation."""
        self.validate_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle with validation."""
        self.validate_integer("x", value, zero_allowed=True)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle with validation."""
        self.validate_integer("y", value, zero_allowed=True)
        self.__y = value

    def validate_integer(self, name, value, zero_allowed=False):
        """
        Validate that a value is an integer and meets required conditions.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.
            zero_allowed (bool): True if 0 is a valid value (for x and y).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not > 0 (or >= 0 if zero_allowed).
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if zero_allowed:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance using `#` characters."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update attributes using positional or keyword arguments."""
        attrs = ["id", "width", "height", "x", "y"]

        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
