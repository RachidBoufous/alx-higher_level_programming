#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function to replace element in list using index

    Args:
        my_list (list): list that we will be using
        idx (integer): index in where we will replace
        element (integer): the elment that we will replace with
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
