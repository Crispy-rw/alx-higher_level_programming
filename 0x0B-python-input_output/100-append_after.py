#!/usr/bin/python3
"""
Contains definition of the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing a specific
       string

    Args:
        filename (str): name of string
        search_string (str): sub-string to be searched for in the file
        new_string (str): string to be inserted
    """

    with open(filename, mode="r+", encoding="UTF-8") as f:
        line = f.read()

    lines = line.split("\n")
    new = []
    for i, l in enumerate(lines):
        new.append(l)
        if i != len(lines) - 1:
            new.append("\n")
        if search_string in l:
            new.append(new_string)

    new_string = ''.join(new)
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(new_string)
