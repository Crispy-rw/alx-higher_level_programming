#!/usr/bin/python3
import sys
if __name__ == "__main__":

    ac = len(sys.argv) - 1

    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(ac))
        exit()

    if len(sys.argv) - 1 == 1:
        print("{} argument:".format(ac))
        for x in sys.argv[1:]:
            print("{}: {}".format(ac, x))

    if len(sys.argv) - 1 > 1:
        print("{} arguments:".format(ac))
        for x, n in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(x, n))
