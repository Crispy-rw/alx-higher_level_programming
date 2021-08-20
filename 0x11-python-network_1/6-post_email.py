#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response with Requests library
"""
import requests
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], email)
    print(r.text)
