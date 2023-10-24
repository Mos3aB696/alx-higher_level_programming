#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """Square class"""

    def __init__(self, size):
        """(constrator)"""
        self.__size = size
