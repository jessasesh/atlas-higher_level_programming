#!/usr/bin/python3
# Replaces an element n list

def new_in_list(my_list, idx, element):
    r_list = my_list.copy()
    if idx < 0:
        return r_list
    if idx >+ len(my_list):
        return r_list
    r_list[idx] = element
    return r_list

