#!/usr/bin/python3
"""A module that contains a function called inherits_from"""


def inherits_from(obj, a_class):
    """A function that returns true if obj is an instance of a_class

    Args:
        obj(): object
        a_class(): class

    Returns:
        TRue or false
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
