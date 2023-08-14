#!/usr/bin/python3
"""a module that has a function to check for attributes"""


def add_attribute(obj, name, val):
    """a func that checks if we can add an atrr"""
    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = val
    else:
        raise TypeError("can't add new attribute")
