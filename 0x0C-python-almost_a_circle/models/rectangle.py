#!/usr/bin/python3
"""
This module defines the Rectangle class
"""
from .base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width Getter Function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter Function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height Getter Function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height Setter Function"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x Getter Function"""
        return self.__x

    @x.setter
    def x(self, value):
        """x Setter Function"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y Getter Function"""
        return self.__y

    @y.setter
    def y(self, value):
        """y Setter Function"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Rectangle Area Function"""
        return self.width * self.height

    def display(self):
        """Print the square with the # character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        str_one = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        str_two = f"{self.width}/{self.height}"
        return f"{str_one} - {str_two}"

    def update(self, *args, **kwargs):
        """updated"""
        if args is not None and len(args) != 0:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Rectangle instance to dictionary """
        attributes = ["id", "width", "height", "x", "y"]
        dictionary = {}

        for key in attributes:
            dictionary[key] = getattr(self, key)

        return dictionary
