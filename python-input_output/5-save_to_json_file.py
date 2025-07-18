#!/usr/bin/python3
"""Function that writes an Object to a text file using Json representation"""


import json


def save_to_json_file(my_obj, filename):
    """Opening a file and using both file.write and serialization"""
    with open(filename, 'w', encoding="utf-8") as file:
        return json.dump(my_obj, file)
