#!/usr/bin/python3
""" class Base """
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON
        string of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dictionary = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dictionary.append(list_objs[i].to_dictionary())

        result = cls.to_json_string(list_dictionary)

        with open(filename, "w") as file:
            file.write(result)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an
        instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dictionaries = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dictionary) for dictionary in list_dictionaries]
