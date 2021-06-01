#!/usr/bin/python3
"""
A script that adds all its arguments to a list and saves them to a file in JSON
format.
"""

import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

data = []
filename = "add_item.json"
try:
    data = load_from_json_file(filename)
except Exception as e:
    for arg in argv[1:]:
        data.append(arg)
    save_to_json_file(data, filename)
else:
    for arg in argv[1:]:
        data.append(arg)
    save_to_json_file(data, filename)
