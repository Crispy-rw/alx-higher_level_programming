#!/usr/bin/python3
""" class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ method """
        return ('[Square] ({}) {}/{} - {}').format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter """
        return self.width

    @size.setter
    def size(self, value):
        """ setter, validations """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Public method that assigns a key/value argument to attributes """
        if len(args) is not 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Public method that returns the dictionary
        representation of a Square"""
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.size
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
