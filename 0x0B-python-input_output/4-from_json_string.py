#!/usr/bin/python3
"""
Contains the definition of the from_json_string function
"""
import json


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON string

    Args:
        my_str (JSON string): Json string to be converted to Python object
    """

    return json.loads(my_str)
