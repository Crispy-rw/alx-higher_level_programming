#!/usr/bin/python3
'''
    check if a object is from a especific subclass
'''


def inherits_from(obj, a_class):
    '''
        check if object belongs a class or heritance but not a superclass
        args:
            obj: object
            a_class: class to check
        Return:
            True or false
    '''
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
