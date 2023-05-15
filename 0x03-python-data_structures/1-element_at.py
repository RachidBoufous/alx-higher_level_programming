#!/usr/bin/python3

def element_at(my_list, idx):
    """a function that returns an element
    at a given index
    Args:
        my_list (list): list of integers
        idx (integer): index to locate an element in list
    """

    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
