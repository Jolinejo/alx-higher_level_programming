#!/usr/bin/python3
"""
100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """func to append text

    Args:
        filename
        search_string
        new_string
    """
    s = ""
    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, mode="w", encoding="utf-8") as myfile:
        myfile.write(s)
