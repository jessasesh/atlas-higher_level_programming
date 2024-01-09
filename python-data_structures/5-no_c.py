#!/usr/bin/python3
# Removes all characters c and C from a string
def no_c(my_string):
    d = {ord(char): None for char in "cC"}

    n_string = my_string.translate(d)
    return n_string
