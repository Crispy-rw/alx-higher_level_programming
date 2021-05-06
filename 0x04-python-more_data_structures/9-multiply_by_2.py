#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary2 = {}
    for key, val in a_dictionary.items():
        a_dictionary2[key] = 2 * val
    return(a_dictionary2)
