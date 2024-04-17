#!/usr/bin/python3
""" This is an empty class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a subclass of BaseGeometry. """
    def __init__(self, width, height):
        """ Instantiation of width and height. """
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
