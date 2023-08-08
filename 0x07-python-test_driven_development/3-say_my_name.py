#!/usr/bin/python3
"""A module for a function that prints the name.

The function takes two args:
    first name
    second name

Both names should be strings.
"""


def say_my_name(first_name, last_name=""):
    """A function that prints first and last name.

    Args:
        first_name(str): first name
        last_name(str): optional last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
