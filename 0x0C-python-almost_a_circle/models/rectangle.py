#!/usr/bin/python3
""" This module contains a class Rectangle. """
from models.base import Base


class Rectangle(Base):
    """ This classs inherits from base.
    it sets its own attributes and calls the super class
    id from base. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the class constructor for rectangle. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter. """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter. """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter. """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter. """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter. """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter. """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This function returns the area value of the Rectangle instance. """
        return self.__width * self.__height

    def display(self):
        """ display rectangle with #. """
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """ Rteyruns a string representation. """
        return (
                "[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ This function  assigns an argument to each attribute. """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                else:
                    break

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ This returns the dictionary representation of a Rectangle. """
        return ({
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            })
