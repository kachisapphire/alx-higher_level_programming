#!/usr/bin/python3
""" This module contains a class student. """


class Student:
    """ This class contains a few parameters. """
    def __init__(self, first_name, last_name, age):
        """ instantiator of class student. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ this function retrieves a dictionary
        representation of a Student instance. """
        return {
                "first
