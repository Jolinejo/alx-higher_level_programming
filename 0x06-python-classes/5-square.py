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

    def my_print(self):
        """prints the square.

        Note: if __size is 0 print an empty line.
        """
        if self.__size == 0:
            print("")
        for i in range(1, self.__size+1):
            for j in range(0, self.__size):
                print("#", end='')
            print("")
