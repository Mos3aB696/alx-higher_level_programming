#!/usr/bin/python3
"""This Is Rectangle Class"""


class Rectangle:
    """This Is Rectangle Class"""

    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that is a square w/ h==w==size"""
        return cls(size, size)

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
