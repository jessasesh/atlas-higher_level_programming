#!/usr/bin/python3
# Function that returns a new dictionary 
# with all values multiplied by 2
def multiply_by_2(my_dict):
    return {key: value * 2 for key, value in my_dict.items()}
