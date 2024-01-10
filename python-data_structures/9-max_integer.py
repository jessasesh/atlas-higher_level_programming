#!/usr/bin/python3
# Function that finds the biggest integer of a list

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    # Sort list in ascending order
    my_list.sort()
    # Returns last element in sorted list
    return my_list[-1]
