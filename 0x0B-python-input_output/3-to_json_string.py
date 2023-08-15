#!/usr/bin/python3
"""a module that has a function"""


def to_json_string(my_obj):
    """Func to read files

    Args:
        filename: file
    """
    data = json.dumps(my_obj)
    return data
