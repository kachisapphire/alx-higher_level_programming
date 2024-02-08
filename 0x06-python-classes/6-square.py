#!/usr/bin/python3
""" This module contains a class.
"""


class Square:
    """ This is a class Square.
    It is made up of attributes and instances.
    """
    def __init__(self, size=0, position=(0, 0)):

        """ This is a documentation for the function.
        Parameter:
            size: initialised to zero.
            position: initialised to 0
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ This function is a getter method for size.
        Returns:
            size of class Sqaure.
        """
        return self.__size

    @property
    def position(self):
        """ This function is a getter for position.
        Returns:
            position of class square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ This function is the setter method for size.
        parameter:
            value: placeholder for size.
        Raises:
            TypeError or ValueError.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ this function is the setter for position.
        parameter:
            value: placeholder for position.
        Raises:
            TypeError if not a tuple of two postive int.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """ This function calculates the area of Square.
        Returns:
            area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """ This function prints a square as #.
        it prints nothing if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

