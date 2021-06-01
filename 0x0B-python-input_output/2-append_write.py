#!/usr/bin/python3
"""
Contains the definition of the append_write function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of the text file and returns the
       number of chars written

    Args:
        filename (str): name of the file to be written to
        text (str): text to be appended to the end of the file
    """

    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
