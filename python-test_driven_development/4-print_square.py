#!/usr/bin/python3
"""
This module defines a function that prints a square with '#'.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Doctests:
    >>> print_square(3)
    ###
    ###
    ###
    >>> print_square(0)

    >>> print_square(1)
    #
    >>> print_square(-3)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    >>> print_square(2.5)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

