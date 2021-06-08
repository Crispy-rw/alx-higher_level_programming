#!/usr/bin/python3
"""
Contains the definition of class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Definition of class Rectangle that represents a rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Initialize and return width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Initialize and return height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Initialize and return x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Initialize and return y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Return the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with # character"""
        for n in range(self.y):
            print()
        for n in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return string object representing the class Rectangle instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Args:
            args (pointer): a "pointer" to an array of strings
            kwargs (double pointer): "double pointer" to a dictionary that has
                                     keyword:value pairs
        """
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        if kwargs is not None and len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns dictionary representation of instance of class Rectangle"""
        keys = ["id", "width", "height", "x", "y"]
        return {a: getattr(self, a) for a in keys}
