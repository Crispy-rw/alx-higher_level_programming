#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        total = 0
        for idx in range(x):
            if type(my_list[idx]) != int:
                continue
            print("{:d}".format(my_list[idx]), end='')
            total += 1
        print("")
        return total
    except (ValueError, TypeError):
        pass
