#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """delete keys with a specific value in a dictionary

    Args:
        a_dictionary (dict): dictionary
        value (any): value to delete

    Returns:
        dict: updated dictionary
    """
    for key, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
