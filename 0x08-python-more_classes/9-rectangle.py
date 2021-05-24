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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the atrubuttes of the rectangle class
        Args:
            width (int, optional): widht of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rectangle += str(self.print_symbol) * self.width + '\n'
        rectangle += str(self.print_symbol) * self.width
        return rectangle

    def __repr__(self):
        """returns area or rectangle using __repr__
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """print message when instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        static method to define the biggest rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''
        define a square from rectangle
        '''
        return cls(size, size)
