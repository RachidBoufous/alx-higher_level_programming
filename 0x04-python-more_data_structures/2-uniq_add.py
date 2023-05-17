#!/usr/bin/python3

def uniq_add(my_list=[]):
    """sum of unique items

    Args:
        my_list (list of integers, optional): list of integers,
        maybe repeated. Defaults to [].

    Returns:
        int: the result of the sum of unique items
    """
    set1 = set(my_list)
    sum = 0
    for i in set1:
        sum += i
    return sum
