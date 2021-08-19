#!/usr/bin/python3
"""find the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function that accepts a list and finds the peak """
    if list_of_integers is None or list_of_integers == []:
        return (None)
    return (do_find_peak(list_of_integers, 0, len(list_of_integers)))


def do_find_peak(lst, l, e):
    """ really find the peak where the first & last index given """

    m = int((l + e) / 2)
    h = e - 1
    if ((m == 0 or lst[m] >= lst[m - 1]) and (m == h or lst[m] >= lst[m + 1])):
        return lst[m]
    elif (m > 0 and lst[m - 1] > lst[m]):
        return do_find_peak(lst, l, m - 1)
    else:
        return do_find_peak(lst, m + 1, e)
