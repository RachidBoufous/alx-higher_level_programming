#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """replace or add key/value in a dictionary

    Args:
        a_dictionary (dict): dictionary
        key (str): key to add or replace
        value (str): value to add or replace

    Returns:
        dict: updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary