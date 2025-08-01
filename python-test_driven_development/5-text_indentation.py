#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines
after each '.', '?', or ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
    >>> text_indentation("Hello. My name is Dianah: Do you know me?")
    Hello.
    <BLANKLINE>
    My name is Dianah:
    <BLANKLINE>
    Do you know me?
    <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".:?":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

