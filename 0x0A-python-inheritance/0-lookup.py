#!/usr/bin/python3
"""A module that has the function LOOKUP"""


def lookup(obj):
    """A func that returns all available atts and methods.

    Args:
        obj

    Returns:
        list of atts and methods."""
    return dir(obj)
