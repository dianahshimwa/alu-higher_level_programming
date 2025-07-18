#!/usr/bin/python3
"""Function that create a python object from a JSON file"""


import json


def load_from_json_file(filename):
    """Opening a JSON file and deserialising ot object using json.loads"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
