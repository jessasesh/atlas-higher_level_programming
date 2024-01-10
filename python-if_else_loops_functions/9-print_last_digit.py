#!/usr/bin/python3
# Function that prints last digit of number
def print_last_digit(number):
    if number < 0:
        number = number * -1
    x = number % 10
    print("{:d}".format(x), end="")
    return x
