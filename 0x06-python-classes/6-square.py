#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """(constrator)"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method"""
        if (type(value) is not tuple or len(value) != 2
                or not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """method that return current square area"""
        return self.size ** 2

    def my_print(self):
        """print method"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print(
                ("\n".join(" " * self.position[0] +
                           "#" * self.size for _ in range(self.size))))
