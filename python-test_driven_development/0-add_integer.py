#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Returns the sum of a and b after casting them to integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

