#!/usr/bin/python3
"""a module that has a function"""

import json


def from_json_string(my_str):    
    """Func to read files

    Args:
        filename: file
    """
    data = json.loads(my_str)
    return data
