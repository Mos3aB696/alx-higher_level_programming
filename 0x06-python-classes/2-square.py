#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """(constrator)"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
