#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) in range(97, 123):
            new = ord(x) - 32
        else:
            new = ord(x)
        print('{:c}'.format(new), end="")
    print()
