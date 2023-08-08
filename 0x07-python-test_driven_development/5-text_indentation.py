#!/usr/bin/python3
"""This module contains a function for indentation

The function takes a string and splits it

splitting happens at : . and ?
"""


def text_indentation(text):
    """A function for printing the string splitted.

    Args:
        text(str): the string to print

    Notes:
        Raises a TypeError if text not str.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    line = ""
    for i in range(len(text)):
        if text[i] in ".?:":
            line += text[i]
            for i in range(len(line)):
                if line[i] != " ":
                    print("{}\n".format(line[i:]))
                    line = ""
                    break
        else:
            line += text[i]
    if line != "":
        start = None
        _end = None
        for i in range(len(line)):
            if line[i] != " ":
                start = i
                break
        for i in range(len(line), 0, -1):
            if line[i-1] != " ":
                _end = i
                break
        if start is not None:
            print("{}".format(line[start: _end]), end='')
