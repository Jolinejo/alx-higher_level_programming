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
    def __init__(self, size=0):
        """Constructor function.

        Note: raise exceptions if size is not int.

        Args:
            size (int): The size from the user.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """function to calc the area.

        Returns:
            Area of the square.
        """
        return self.__size*self.__size
