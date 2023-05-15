#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """function that prints all integers of a list.

    Args:
        my_list (list, optional): _description_. Defaults to [].
    """
    for i in my_list:
        print("{:d}".format(i))
