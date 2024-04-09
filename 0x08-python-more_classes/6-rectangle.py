#!/usr/bin/python3
""" This module contains a class rectangle. """


class Rectangle:
    """ This is a class rectangle that defines a rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ This function is the instantiation for Rectangle.
        Parameters: (width, height). """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            rectangle = []
            for i in range(self.height):
                [rectangle.append('#') for j in range(self.width)]
                if i != self.height - 1:
                    rectangle.append("\n")
            return ("".join(rectangle))

    def __repr__(self):
        rectangle = "Rectangle(" + str(self.width)
        rectangle += ", " + str(self.height) + ")"
        return rectangle

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
