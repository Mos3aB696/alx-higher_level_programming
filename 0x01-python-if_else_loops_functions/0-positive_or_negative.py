#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:  # use str() to convert int to str and make concat
    print(str(number) + " is negative")
elif number > 0:  # use placeholder with format
    print("{} is positive".format(number))
else:
    print("{} is zero".format(number))
