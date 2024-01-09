#!/usr/bin/python3
"""Prints all integers of a list, in reverse order
Args:
    my_list: the input list
Return: reordered list
"""
def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{:d}".format(num))
