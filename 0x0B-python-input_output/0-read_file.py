#!/usr/bin/python3
"""a module that has a function"""


def read_file(filename=""):
    """Func to read files

    Args:
        filename: file
    """
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read())
