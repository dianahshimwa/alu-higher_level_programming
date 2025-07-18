#!/usr/bin/python3
"""Function that returns the dictionary instance description"""


def class_to_json(obj):
    """Using return parameter+instance"""
    return obj.__dict__
