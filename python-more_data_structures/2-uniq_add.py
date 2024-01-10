#!/usr/bin/python3
# Function that adds all unique integers in a list

def uniq_add(my_list=[]):
    add = 0
    for u_elements in set(my_list):
        add += u_elements
    return add
