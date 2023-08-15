#!/usr/bin/python3
"""a module that has a function"""


def class_to_json(obj):
    """Func to read files

    Args:
        filename: file
    """
    data = (obj.__dict__)
    return data
