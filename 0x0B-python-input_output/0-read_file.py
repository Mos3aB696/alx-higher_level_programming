#!/usr/bin/python3
"""Function That Reads Text"""


def read_file(filename=""):
    """Function That Read File Content"""
    with open(filename, 'r', encoding="UTF-8") as file:
        file.read()
