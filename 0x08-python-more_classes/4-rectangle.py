#!/usr/bin/python3
"""define a rectangle class
"""


class Rectangle:
    """represents a rectangle class
    Raises:
        TypeError: weidth must be an integer
        ValueError: weidht must be equal o greater than zero
        TypeError: height must be an integer
        ValueError: height must be equal or greater than zero
    """
    def __init__(self, width=0, height=0):
        """initialize the atrubuttes of the rectangle class
        Args:
            width (int, optional): widht of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to define the are of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """method to define the perimeter o rectangle
        """
        if self.width is 0 or self.height is 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """returns area or rectangle
        """
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle
        for i in range(self.height - 1):
            rectangle += "#" * self.width + '\n'
        rectangle += "#" * self.width
        return rectangle

    def __repr__(self):
        """returns area or rectangle using __repr__
        """
        return "Rectangle({}, {})".format(self.width, self.height)
