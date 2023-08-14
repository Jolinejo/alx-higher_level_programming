#!/usr/bin/python3
"""A module that contains a function called is_same_class"""


def is_same_class(obj, a_class):
    """A function that returns true if obj is an instance of a_class

    Args:
        obj(): object
        a_class(): class

    Returns:
        TRue or false
    """
    return type(obj) == a_class
