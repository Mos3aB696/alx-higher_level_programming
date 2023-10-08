#!/usr/bin/python3
def no_c(my_string):
    strList = list(my_string)
    newStr = ''
    for i in strList:
        if i == 'c' or i == 'C':
            continue
        newStr += i
    return newStr
