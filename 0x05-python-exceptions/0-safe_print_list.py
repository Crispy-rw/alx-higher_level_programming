#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        total = 0
        for index in my_list[:x]:
            print("{}".format(index), end='')
            total += 1
        print("")
        return total

    except something_wrong:
        print("Something went wrong")
