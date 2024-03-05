#!/usr/bin/python3
""" This module contains the class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ This is the class rectangle which
    inherits from class base with a number of
    attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the isnatntiator for class rectangle.
        parameters:
            width: width of the rectangle.
            height: height of the rectangle.
            X: int
            y: int
            id: identity of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """ getter/setter for width."""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """ getter for height."""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """ getter for x"""
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """ getter fot y"""
            return self.__y

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
