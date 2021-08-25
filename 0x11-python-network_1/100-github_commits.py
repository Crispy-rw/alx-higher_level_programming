#!/usr/bin/python3
'''
Script that list 10 commits from the most recent to oldest of the repository
rails by the user rails
'''

if __name__ == "__main__":
    from sys import argv
    from requests import get
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    req = get(url)

    for i in range(10):
        print("{sha}: {author[login]}".format(**req.json()[i]))
