#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list
    Args:
        my_list: the list
        idx: the index
    Returns: the value in index
    """
    if idx < 0:
        return None
    elif idx not in range(len(my_list)):
        return None
    else:
        return my_list[idx]
