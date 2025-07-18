#!/usr/bin/python3
"""Writing a class which defines student"""


class Student:
    """The public attributes"""
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """Initialised the attributes for the needed data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returning the dictionary of the data"""
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return context
