#!/usr/bin/python3
"""a module that has a function"""


def write_file(filename="", text=""):
    """Func to read files

    Args:
        filename: file
    """
    r = 0
    with open(filename, mode="w+", encoding="utf-8") as myfile:
        r += myfile.write(text)
    return r
