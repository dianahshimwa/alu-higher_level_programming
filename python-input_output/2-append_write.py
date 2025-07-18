#!/usr/bin/python3
"""Function that appends a string at the end of the file utf-8"""


def append_write(filename="", text=""):
    """Appending into the file using write and a"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
