#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class the defines a square.

    Args:
        size (noval): The size of the square.

    Attributes:
        __size: Private attribute size.
    """
    def __init__(self, size):
        """Constructor function

        Args:
            size (noval): The size from the user.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
