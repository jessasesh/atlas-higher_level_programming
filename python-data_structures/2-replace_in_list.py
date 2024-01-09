#!/usr/bin/python3
"""
Replaces an element of a list at a specific position
Args:
    my_list: input list
    idx: index to replace
    element: new element
    
Returns: modified list
"""

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
