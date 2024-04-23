#!/usr/bin/python3
""" this is a module containing a class base. """
import json
import csv


class Base:
    """ This class has a private attribute __nb_object.
    it takes in the parameter id.
    it is the base of all the other projects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This si the instantiator for class Base. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ this function returns the JSON string representation. """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ this function writes the JSON string representation. """
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = []
                for i in list_objs:
                    dict_list.append(i.to_dictionary())
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ this function returns list of the JSON string representation. """
        if json_string is None or json_string == "":
            return ("[]")
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ this function returns an instance with all attributes. """
        if dictionary:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ this function returns a list of instances. """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r") as f:
                dict_list = Base.from_json_string(f.read())

                lists = []

                for i in dict_list:
                    lists.append(cls.create(**i))
                return lists
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ this function is for serialization. """
        filename = "{}.csv".format(cls.__name__)

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    instances = ["id", "width", "height", "x", "y"]
                else:
                    instances = ["id", "size", "x", "y"]
                csvwrite = csv.DictWriter(f, fieldnames=instances)

            for i in list_objs:
                csvwrite.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ this function is for deserialization. """
        filename = "{}.csv".format(cls.__name__)

        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    instances = ["id", "width", "height", "x", "y"]
                else:
                    instances = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(f, fieldnames=instances)
                lists = []
                for i in dict_list:
                    i = {key: int(value) for key, value in i.items()}
                    new_list = cls.create(**i)
                    lists.append(new_list)
                return lists
        except FileNotFoundError:
            return []
