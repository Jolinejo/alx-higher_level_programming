#!/usr/bin/python3
"""This is a module that contains print_square

Print_square is a fuction that prints a square and takes a size.
The size must be an int or else raise TypeError.
"""


def print_square(size):
    """A function that prints a square.

    Args:
        size(int): size of the square to be printed.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
