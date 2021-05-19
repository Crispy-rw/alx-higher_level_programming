#!/usr/bin/python3
"""Contains a definition of a class Square."""


class Square:
    """Definition of a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an object of the class Square.

        Ensures that the parameter passed is of type int and is not less than 0

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is tuple and (len(position) == 2 and
                                        type(position[0]) is int and
                                        type(position[1]) is int and
                                        position[0] >= 0 and position[1] >= 0):
                    self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Returns the value of the size attribute

        Setter method sets the value of size to value
        Ensures that the parameter passed is of type int and is not less than 0

        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the value of the attribute position.

        Setter method sets the value of the position attribute.
        Ensures the parameter passed is a tuple of 2 integers.
        """

        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and (len(value) == 2 and
                                     type(value[0]) is int and
                                     type(value[1]) is int and
                                     value[0] >= 0 and value[1] >= 0):
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square's area"""

        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character '#'.
        Takes into account the position attribute to determine where to print
        the square.
        """

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for n in range(0, self.__size):
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)

    def __str__(self):
        """Prints in stdout the square with the character '#'.
        Takes into account the position attribute to determine where to print
        the square.
        """

        res = []
        if self.__size == 0:
            pass
        else:
            for i in range(0, self.__position[1]):
                res.append('\n')
            for n in range(0, self.__size):
                for l in range(0, self.__position[0]):
                    res.append(' ')
                for k in range(0, self.__size):
                    res.append('#')
                if n != self.__size - 1:
                    res.append('\n')
        return ''.join(res)
