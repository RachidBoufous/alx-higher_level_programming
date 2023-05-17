#!/usr/bin/python

def only_diff_elements(set_1, set_2):
    """return diff elements in both sets

    Args:
        set_1 (set): set 1
        set_2 (set): set 2

    Returns:
        list: diff elements
    """
    diffElements = []
    for i in set_1:
        if i not in set_2:
            diffElements.append(i)
    return diffElements
