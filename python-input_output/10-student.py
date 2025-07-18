#!/usr/bin/python3
"""Creating a class Student basing on file 9-student.py"""


class Student:
    """The classes"""
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """Initialising the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returning a dictionary rep of the data"""
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        if attrs is None or type(attrs) != list:
            return context
        else:
            cont = {}
            for item in attrs:
                if type(item) != str:
                    return context
                if item in context.keys():
                    cont[item] = context[item]
            return cont
