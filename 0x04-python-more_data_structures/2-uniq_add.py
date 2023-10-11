#!/usr/bin/python3
def uniq_add(my_list=[]):

    # the normal way
    # theSet = set(my_list)
    # sum = 0
    # for i in theSet:
    #    sum += i
    # return sum

    # solve task with one line
    return sum(set(my_list))
