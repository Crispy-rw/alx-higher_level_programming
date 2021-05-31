#!/usr/bin/python3
'''
    Class enheritance from list
'''


class MyList(list):
    '''
        print a list sorted
    '''
    def print_sorted(self):
        print(sorted(self))
