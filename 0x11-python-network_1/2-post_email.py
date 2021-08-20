#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
