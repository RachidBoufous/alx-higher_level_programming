#!/usr/bin/python3

def safe_print_division(a, b):
    """safely prints an integer

    Args:
        a (integer): integer to divide
        b (integer): integere to divide on
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
