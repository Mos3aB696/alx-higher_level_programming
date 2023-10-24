#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """The init function (constrator)"""
        self.__size = size

    @property
    def size(self):
        """get_size function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """function that return current square area"""
        return self.size ** 2

    def my_print(self):
        """print the #"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
