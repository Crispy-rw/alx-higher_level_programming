#!/usr/bin/python3
'''
    function to set an atributte
'''


def add_attribute(obj, name, value):
    '''
        add an antributte or raise an error when object has not attributes
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
