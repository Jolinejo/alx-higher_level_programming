#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""


class Square:
    """A class the defines a square.

    Args:
        size (int): The size of the square.
        position (tuple): positioning the square.

    Attributes:
        __size: Private attribute size.
        __position: position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor function.

        Note: raise exceptions if size is not int.

        Args:
            size (int): The size from the user.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Getter for __position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of __position.

        Args:
            value (tuple): value of __position.

        Raises:
            TypeError: if not int.
        """
        if type(value) != tuple or len(value) != 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square.

        Note: if __size is 0 print an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for x in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
