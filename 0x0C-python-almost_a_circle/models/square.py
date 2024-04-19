#!/usr/bin/python3
""" This module contains a square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is a subclass that inherits from rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor of square. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size. """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ this function that assigns attributes. """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    break

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """ string representation. """
        return ("[Square] ({}) {}/{} - "
                "{}".format(self.id, self.x, self.y, self.height))

    def to_dictionary(self):
        """ return dictionary representation. """
        return ({
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            })
