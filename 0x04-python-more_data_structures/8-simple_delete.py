#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """delete key in a dictionary

    Args:
        a_dictionary (dict): dictionary
        key (str, optional): key to delete. Defaults to "".

    Returns:
        dict: updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
