#!/usr/bin/python3
"""
    Class file.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ Class abstract of Shape. """

    @abstractmethod
    def area(self):
        """ Calculate the area. """
        pass

    @abstractmethod
    def perimeter(self):
        """ Calculate the perimeter. """
        pass


class Circle(Shape):
    """ Class Circle inherited of Shape. """

    def __init__(self, radius):
        """ Initialize a circle. """
        self.__radius = radius

    def area(self):
        """ Calculate the area. """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """ Calculate the perimeter. """
        return math.pi * 2 * self.__radius


class Rectangle(Shape):
    """ Class Rectangle inherited of Shape. """

    def __init__(self, width, height):
        """ Initialize a rectangle. """
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate the area. """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the perimeter. """
        return (self.__width + self.__height) * 2


def shape_info(obj):
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
