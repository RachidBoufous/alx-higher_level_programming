#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """find element in list and replace it

    Args:
        my_list (list): list of items
        search (integer): element to search for
        replace (integer): element to replace with
    """

    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
