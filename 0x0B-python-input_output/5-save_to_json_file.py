#!/usr/bin/python3
"""a module that has a function"""

import json


def save_to_json_file(my_obj, filename):
    """Func to read files

    Args:
        filename: file
    """
    data = json.dumps(my_obj)
    with open(filename, 'w+') as f:
        json.dump(data, f)
