#!/usr/bin/python3
"""[summary]
"""


def text_indentation(text):
    """indentation a string
    Args:
        text (str): [string]
    """
    begin = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for i, j in enumerate(text):
        if j in '.?:':
            print(text[begin: i + 1].strip() + '\n')
            begin = i + 1
    if begin < len(text):
        print(text[begin:].strip(), end="")
