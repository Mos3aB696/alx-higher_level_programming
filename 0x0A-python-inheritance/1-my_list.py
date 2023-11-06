#!/usr/bin/python3
"""This Is MyList Class"""


class MyList(list):
    """ subclass of list"""

    def __init__(self):
        """init the object"""
        super().__init__()

    def print_sorted(self):
        """Sorted Method"""
        print(sorted(self))
