#!/usr/bin/python3
"""Defining the class square"""


class Square:
    """ Creating a private instance """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        square_area = self.__size ** 2
        return square_area

    @property
    def size(self):
        """Method that returns the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that set the size value of the square object """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
