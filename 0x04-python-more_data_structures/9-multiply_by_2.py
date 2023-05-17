#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """multiply all values in a dictionary by 2

    Args:
        a_dictionary (dict): dictionary

    Returns:
        dict: updated dictionary
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
