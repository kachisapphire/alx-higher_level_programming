#!/usr/bin/python3
""" This is an empty class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a subclass of BaseGeometry. """
    def __init__(self, width, height):
        """ Instantiation of width and height. """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ This implements the area function. """
        return self.__width * self.__height

    def __str__(self):
        """ function returns string and print representation. """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
