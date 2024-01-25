#!/usr/bin/python3
# Find a peak in a list of unsorted integers.
def find_peak(lst):
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
