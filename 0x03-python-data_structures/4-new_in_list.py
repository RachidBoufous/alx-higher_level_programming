#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace an element in liust

    Args:
        my_list (list): original list
        idx (integer): index in which we replace at
        element (integer): the element to replace with at idx
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
