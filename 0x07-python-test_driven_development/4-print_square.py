#!/usr/bin/python3
"""
function to print a square of size
"""


def print_square(size):
    """prints a square
    Args:
        size (int): size of square
    Raises:
        TypeError: must be an integer
        ValueError: must be greater o equal zero
        TypeError: must be an integer
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
