#!/usr/bin/python3
"""Rectangle module that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        self.validate_integer("width", width, False)
        self.validate_integer("height", height, False)
        self.validate_integer("x", x)
        self.validate_integer("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @staticmethod
    def validate_integer(name, value, can_be_zero=True):
        """Validate an integer value based on given rules.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.
            can_be_zero (bool): Whether zero is allowed.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is not > 0 or >= 0 as per rules.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if can_be_zero:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    @property
    def width(self):
        """Get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Get x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Get y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using `#`, respecting x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Update attributes using args or kwargs.

        Args:
            *args: id, width, height, x, y (in that order)
            **kwargs: key/value pairs for attributes
        """
        attr_list = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for attr, val in zip(attr_list, args):
                setattr(self, attr, val)
        else:
            for key, val in kwargs.items():
                if key in attr_list:
                    setattr(self, key, val)
