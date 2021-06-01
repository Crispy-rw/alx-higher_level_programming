#!/usr/bin/python3
"""
Contains defintion of the class_to_json function
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures for JSON
       serialization of an object

    Args:
        obj (unknown): class instance object to be serialized to JSON a string
    """

    return obj.__dict__
