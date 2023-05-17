#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """multiply all elements of a list

    Args:
        my_list (list, optional): list. Defaults to [].
        number (int, optional): number to multiply. Defaults to 0.

    Returns:
        list: updated list
    """
    return (list(map((lambda i: i * number), my_list)))
