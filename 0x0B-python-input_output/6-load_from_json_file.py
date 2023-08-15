#!/usr/bin/python3
"""a module that has a function"""

import json


def load_from_json_file(filename):
    """Func to read files

    Args:
        filename: file
    """
    with open(filename) as f:
      return  json.load(f)
