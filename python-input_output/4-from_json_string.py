#!/usr/bin/python3
"""Function that returns a python object represented by a JSON string"""


import json


def from_json_string(mystr):
    """Object representation using json.loads"""
    return json.loads(mystr)
