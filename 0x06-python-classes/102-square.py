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

    @property
    def size(self):
        """Getter for __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of __size.

        Args:
            value (int): value of __size.

        Raises:
            ValueError: if < 0.
            TypeError: if not int.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """equal operator."""
        return self.__size == other.__size

    def __lt__(self, other):
        """less than operator."""
        return self.__size < other.__size

    def __le__(self, other):
        """less equal operator."""
        return self.__size <= other.__size

    def __gt__(self, other):
        """greater than operator."""
        return self.__size > other.__size

    def __ge__(self, other):
        """greater equal operator."""
        return self.__size >= other.__size

    def __ne__(self, other):
        """not equal operator."""
        return self.__size != other.__size
