#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""


class Square:
    """A class the defines a square.

    Args:
        size (noval): The size of the square.

    Attributes:
        __size: Private attribute size.
    """
    def __init__(self, size=None):
        """Constructor function

        Args:
            size (noval): The size from the user.
        """
        self.__size = size
