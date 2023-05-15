#!/bin/usr/python3

def no_c(my_string):
    """return string after striping all the C's in it

    Args:
        my_string (string): string with c characters
    """

    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
