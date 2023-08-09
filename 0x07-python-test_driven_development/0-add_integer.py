#!/usr/bin/python3
"""Module for a function that adds two ints.

This module contains a function that adds two ints or floats
but floats are first convirted to ints

the result value is an int.
"""


def add_integer(a, b=98):
    """Addition func.

    Note: raises exception if not int or float

    Args:
        a(int, float): first arg
        b(int, float): optional arg

    Returns:
        Sum of the two nums.
    """
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
