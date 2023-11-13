#!/usr/bin/python3
from .base import Base
"""
This module defines the Rectangle class that inherits from Base.
The Rectangle class has private instance attributes width, height, x, and y,
each with its own public getter and setter.
"""


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        Parameters:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle. Default is 0.
        y (int): The y coordinate of the new Rectangle. Default is 0.
        id (int): The id of the new Rectangle. If id is None, the new Rectangle
        will be assigned an auto-generated, unique id.
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
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        attributes = ['id', 'width', 'height', 'x', 'y']
        for attribute, value in zip(attributes, args):
            setattr(self, attribute, value)
