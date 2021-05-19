#!/usr/bin/python3
"""Contains the definition for a MagicClass class"""
import math


class MagicClass:
    """Definition of class MagicClass"""
    def __init__(self, radius=0):
        """Initializes an instance of MagicClass class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of the object

        Args:
            math.pi (int): pi
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return circumference of the object

        Args:
            math.pi (int): pi
        """
        return 2 * math.pi * self.__radius
