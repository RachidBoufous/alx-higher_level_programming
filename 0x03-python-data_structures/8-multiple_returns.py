#!/usr/bin/python3

def multiple_returns(sentence):
    """Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module

    Args:
        sentence (string): a string to use for multi-returns
    """
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
