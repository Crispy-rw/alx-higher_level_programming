#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response with Requests library
"""
import requests
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    r = requests.get(argument)
    print(r.headers.get('X-Request-Id'))
