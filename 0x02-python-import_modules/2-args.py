#!/usr/bin/python3
import sys

ac = len(sys.argv)

if __name__ == '__main__':
    if ac == 1:
        print("0 argument.")
    elif ac == 2:
        print("{} argument:".format(ac - 1))
        print("{}: {}".format(ac, sys.argv[1]))
    else:
        print("{} arguments:".format(ac - 1))
        for x, n in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(x, n))
