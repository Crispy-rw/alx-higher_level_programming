#!/usr/bin/python3
"""
Define a class Square
"""


class Square():
    '''
    This class represents a Square.
    '''
    def __init__(self, size=0):
        '''
        Initialization of objects
        Args:
            size(int): size of square, must be integer and greater than zero
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        '''
            property  to retrieve it
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
            property  setter to set it
            Args:
            value : must be an integer and greater than zero"
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
            define a method to get an area of square class
        '''
        return self.__size ** 2
