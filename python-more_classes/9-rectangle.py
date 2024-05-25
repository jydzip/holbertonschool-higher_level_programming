#!/usr/bin/python3
"""
    File for the class Rectangle.
"""


class Rectangle:
    """
        Class that defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Initialization of the Rectangle class.
            Arguments:
                width (int, optional): Width of the rectangle.
                height (int, optional): Height of the rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Get the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter of the width of a rectangle.
            Arguments:
                value (int): Value to add.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get the height of a rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter of the height of a rectangle.
            Arguments:
                value (int): Value to add.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Returns the rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
            Returns the rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        text = ""
        for row in range(self.height):
            for column in range(self.width):
                try:
                    text += str(self.print_symbol)
                except Exception:
                    text += type(self).print_symbol
            if row < self.height - 1:
                text += "\n"
        return text

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
