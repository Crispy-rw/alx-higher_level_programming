#!/usr/bin/python3
'''
    Class empty
'''


class BaseGeometry():
    '''
        Represents a BaseGeometry class
    '''
    def area(self):
        '''
            method to raise exception if area was not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            method to validate value
            Raise TypeError and ValueError
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
