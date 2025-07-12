#!/usr/bin/python3
"""Defining a class called square"""


class Square:
    """Filling the square class"""

    def __init__(self, size=0):
        """Method to initialise the square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
