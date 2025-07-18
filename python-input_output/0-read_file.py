#!/usr/bin/python3
"""Function that reads a file UTF8"""


def read_file(filename=""):
    """reads the content from outside the file"""
    with open(filename, encoding="utf-8") as file:
        content = file.read()
    print(content, end="")
