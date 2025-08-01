#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width getter and setter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        self.__width = value

    # height getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.__height = value

    # x getter and setter
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value, zero_allowed=True)
        self.__x = value

    # y getter and setter
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value, zero_allowed=True)
        self.__y = value

    def validate_integer(self, name, value, zero_allowed=False):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if zero_allowed:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes (in order), or via keyword."""
        attr_order = ["id", "width", "height", "x", "y"]

        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attr_order):
                    setattr(self, attr_order[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
