#!/bin/usr/python3

def no_c(my_string):
    """return string after striping all the C's in it

    Args:
        my_string (string): string with c characters
    """

    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
