#!/usr/bin/python3
"""
Contains the definition of the write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of chars written

    Args:
        filename (str): name of the file to write to
        text (str): text to write to the file
    """

    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
