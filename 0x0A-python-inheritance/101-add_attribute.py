#!/usr/bin/python3
"""a module that has a function to check for attributes"""


def add_attribute(obj, name, val):
    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = val
    else:
        raise TypeError("can't add new attribute")
