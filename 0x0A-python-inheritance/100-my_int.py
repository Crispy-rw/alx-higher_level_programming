#!/usr/bin/python3
'''
new class to truncate the __eq__ and __ne__ methods
'''


class MyInt(int):
    '''
    class My int inherite from int
    '''

    def __init__(self, value):
        '''
        initialize the attribute value
        '''
        self.value = value

    def __eq__(self, other):
        '''
        check the equal value
        returns false
        '''
        return self.value != other

    def __ne__(self, other):
        '''
        check the diferent value
        returns true
        '''
        return self.value == other
