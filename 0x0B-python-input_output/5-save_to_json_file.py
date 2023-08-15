#!/usr/bin/python3
"""a module that has a function"""

import json


def save_to_json_file(my_obj, filename):
    """Func to read files

    Args:
        filename: file
    """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
