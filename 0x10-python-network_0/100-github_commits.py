#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository
Accepts repository name and owner name
"""
import requests
from sys import argv

if __name__ == "__main__":
    u = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    resp = requests.get(u)
    json = resp.json()
    for j in json[:10]:
        print("{}: {}".format(j.get('sha'),
                              j.get('commit').get('author').get('name')))
