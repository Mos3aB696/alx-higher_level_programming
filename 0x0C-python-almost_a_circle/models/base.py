#!/usr/bin/python3
""" class Base """
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that writes the CSV string of list_objs to a file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is not None:
                writer = csv.writer(csvfile)
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """class method that returns a list of instances"""
        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(row[1]),
                                      "height": int(row[2]), "x": int(row[3]),
                                      "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(row[0]), "size": int(
                            row[1]), "x": int(row[2]), "y": int(row[3])}
                    list_objs.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return list_objs
