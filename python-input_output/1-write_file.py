#!/usr/bin/python3
"""Function that writes into a string into a file utf-8"""


def write_file(filename="", text=""):
    """Writing inside the file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
