#!/usr/bin/python3
"""add a (float or int) and b (float or int)
"""


def add_integer(a, b=98):
    '''
    add two numbers
    Args:
    a : int or float
    b : int or float
    Return an int
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)
