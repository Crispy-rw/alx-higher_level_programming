#!/usr/bin/python3
import sys
sums = 0
if __name__ == '__main__':
    for v in sys.argv[1:]:
        sums += int(v)
    print(sums)
