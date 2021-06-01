#!/usr/bin/python3
"""
Contains the definition of the load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a "JSON file"

    Args:
        filename (str): name of the file containg the JSON string
    """

    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
