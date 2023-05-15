#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list.

    Args:
        my_list (list): list of integers

    Returns:
        list: list of booleans
    """
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list