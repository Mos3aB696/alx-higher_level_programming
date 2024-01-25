#!/usr/bin/python3
"""
    The function `find_peak` takes in a list of numbers
    and returns the peak element, which is an
    element that is greater than its adjacent elements.
    :param list_of_integers: The parameter `list_of_integers` is a list of numbers
    :return: the peak element from the given list.
"""


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
