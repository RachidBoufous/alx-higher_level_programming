#!/usr/bin/python3

def best_score(a_dictionary):
    """return key with biggest integer value

    Args:
        a_dictionary (dict): dictionary

    Returns:
        str: key with biggest integer value
    """
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
