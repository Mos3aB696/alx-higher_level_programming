#!/usr/bin/python3
"""This Is Rectangle Class"""


class Rectangle:
    """This Is Rectangle Class"""

    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set Width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """The Rectangle Area"""
        return self.width * self.height

    def perimeter(self):
        """The Rectangel Perimeter"""
        return (self.width + self.height) * 2
