#!/usr/bin/python3
"""This Is MyList Class"""


class MyList(list):
    """MyList Class"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Sorted Method"""
        print(sorted(self))
