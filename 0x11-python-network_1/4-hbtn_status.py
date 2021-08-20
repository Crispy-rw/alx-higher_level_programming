#!/usr/bin/python3
""" Fetching URLs with Requests library """
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    t = r.text
    print("Body response:")
    print("\t- type: {}\n\t- content: {}"
          .format(type(t), t))
