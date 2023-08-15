#!/usr/bin/python3
"""a module that has a function"""

import json


def class_to_json(obj):
    """Func to read files

    Args:
        filename: file
    """
    data = json.dumps(obj.__dict__)
    return data
