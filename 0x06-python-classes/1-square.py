#!/usr/bin/python3
"""
Define a class Square
"""


class Square():
    '''class represents a Square.
        Args:
            size(int): represents the size of square
    '''
    def __init__(self, size):
        '''Initialization of instance attributes
                Args:
                size (int): The size of the square
        '''
        self.__size = size
