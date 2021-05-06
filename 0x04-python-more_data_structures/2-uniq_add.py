#!/usr/bin/python3
def uniq_add(my_list=[]):
    adds = 0
    for i in set(my_list):
        adds += i
    return(adds)
