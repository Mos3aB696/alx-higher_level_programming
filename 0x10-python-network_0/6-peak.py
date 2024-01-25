#!/usr/bin/python3


def find_peak(lst):
    """
    The function `find_peak` takes in a list of numbers
    and returns the peak element, which is an
    element that is greater than its adjacent elements.
    :param lst: The parameter `lst` is a list of numbers
    :return: the peak element from the given list.
    """
    n = len(lst)
    if n == 1:
        return lst[0]
    elif n == 2:
        return max(lst[0], lst[1])
    elif n == 0:
        return None
    mid = n // 2
    if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
        return lst[mid]
    elif lst[mid] <= lst[mid - 1]:
        return find_peak(lst[:mid])
    else:
        return find_peak(lst[mid+1:])
