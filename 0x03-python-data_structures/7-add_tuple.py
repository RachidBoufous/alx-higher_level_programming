#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Returns a tuple with 2 integers:
        The first element should be the addition of the
          first element of each argument
        The second element should be the addition of
        the second element of each argument
        You are not allowed to import any module
        You can assume that the two tuples will only
        contain integers
        If a tuple is smaller than 2, use the value 0
        for each missing integer
        If a tuple is bigger than 2, use only the first 2 integers

    Args:
        tuple_a (tuple, optional): tuple 1. Defaults to ().
        tuple_b (tuple, optional): tuple 1. Defaults to ().
    """

    new_tuple = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
