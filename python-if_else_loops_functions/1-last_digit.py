#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
while True:
    ld = abs(number) % 10
    os = "Last digit of {}, is {}, ".format(number, ld)
    if ld > 5:
        os += "and is greater than 5"
        break
    elif ld == 0:
        os += "and is 0"
    else:
        os += "and is less than 6 and not 0"
    print (os)

    number = random.randint(-10000, 10000)
