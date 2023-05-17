#!/usr/bin/python3

def common_elements(set_1, set_2):
    """return common elements in both sets

    Args:
        set_1 (set): set 1
        set_2 (set): set 2

    Returns:
        list: commun elements
    """

    communItems = []
    for i in set_1:
        if i in set_2:
            communItems.append(i)
    return communItems
