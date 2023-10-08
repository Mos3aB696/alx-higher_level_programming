#!/usr/bin/python3
def max_integer(mylist=[]):
    if mylist:
        maxVal = mylist[0]
        for i in mylist[:]:
            if i > maxVal:
                maxVal = i
        return maxVal
    else:
        return None
