#!/usr/bin/python3

def no_c(my_string):
    """return string after striping all the C's in it

    Args:
        my_string (string): string with c characters
    """

    new_string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            new_string += x
    return new_string
