#!/usr/bin/env python3
def uppercase(str):
    container = ''
    for i in str:
        if ord(i) in range(97, 123):
            container += chr(ord(i) - 32)
        else:
            container += i
    print("{}".format(container))
