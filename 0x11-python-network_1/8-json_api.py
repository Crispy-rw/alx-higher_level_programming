#!/usr/bin/python3
"""
This Python script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) != 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        req = requests.post(url, data={'q': q}).json()
        if len(req) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
    except:
        print('Not a valid JSON')
