#!/usr/bin/python3
"""A module that contains a function called is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """A function that returns true if obj is an instance of a_class

    Args:
        obj(): object
        a_class(): class

    Returns:
        TRue or false
    """
    return isinstance(obj, a_class)
