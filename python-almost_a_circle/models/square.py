#!/usr/bin/python3
"""Square module that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square, which is a special kind of Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): Size of the square's sides.
            x (int): x position.
            y (int): y position.
            id (int): Identity of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
