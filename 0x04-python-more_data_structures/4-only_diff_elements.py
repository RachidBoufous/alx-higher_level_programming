#!/usr/bin/python

def only_diff_elements(set_1, set_2):
    """return diff elements in both sets

    Args:
        set_1 (set): set 1
        set_2 (set): set 2

    Returns:
        set: diff elements
    """
    set3 = set_1 | set_2

    for item in set3.copy():
        if item in set_1 and item in set_2:
            set3.remove(item)
    return set3
