#!/usr/bin/python3
"""Square module that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square, which is a special kind of Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square (width or height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (width and height)."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes using *args or **kwargs.

        Args:
            *args: Non-keyword arguments in the order:
                1st - id
                2nd - size
                3rd - x
                4th - y
            **kwargs: Keyword arguments as key/value pairs.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
