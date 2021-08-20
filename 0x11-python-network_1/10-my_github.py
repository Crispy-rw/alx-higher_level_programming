#!/usr/bin/python3
"""Get id
"""

if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, passwd))
    print(req.json().get('id'))
