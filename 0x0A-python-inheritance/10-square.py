#!/usr/bin/python3
'''
    Class BaseGeometry
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        represents a Square class
    '''
    def __init__(self, size):
        '''
        initialize the square class
        take the init from rectangle class
        take the method integer validator from baseGeometry
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
        define the area to the square
        '''
        return self.__size ** 2
