#!/usr/bin/python3
"""class Square
inheritance of class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        str_one = f"[Square] ({self.id}) {self.x}/{self.y}"
        str_two = f"{self.size}"
        return f"{str_one} - {str_two}"

    def update(self, *args, **kwargs):
        """updated"""
        if args is not None and len(args) != 0:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attributes[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Square instance to dictionary"""
        attributes = ["id", "size", "x", "y"]
        dictionary = {}

        for key in attributes:
            if key == "size":
                dictionary[key] = getattr(self, "width")
            else:
                dictionary[key] = getattr(self, key)

        return dictionary
