#!/usr/bin/python3
import sys

newlist = [int(x) for x in sys.argv[1:]]

if __name__ == '__main__':
    print("{}".format(sum(newlist)))
