#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print the list in reverse

    Args:
        my_list (list, optional): list of integers. Defaults to [].
    """
    for i in my_list[::-1]:
        print("{:d}".format(i), end="\n")
