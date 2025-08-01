#!/usr/bin/python3
"""function that returns true/false if obj is an instance of a_class

   Args:
       obj: object
       a_class: class type

   Returns:
       True if obj is an instance of a_class
       False, otherwise
"""


def inherits_from(obj, a_class):
    """function that returns true/false if obj is an instance of a_class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
