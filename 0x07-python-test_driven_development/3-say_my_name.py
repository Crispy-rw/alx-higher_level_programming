#!/usr/bin/python3
"""function to print a full name with two strings
"""


def say_my_name(first_name, last_name=""):
    """prints a full name
    Args:
        first_name (str): first name
        last_name (str): last name. Defaults to "".
    Raises:
        TypeError: "first_name must be a string"
        TypeError: "last_name must be a string"
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
