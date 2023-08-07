#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""


class Rectangle:
    """A class the defines a rectangle.

    Args:
        width(int): The width of the square.
        height(int): The height of the square.

    Attributes:
        __width: Private attribute width.
        __height: Private attribute height.
    """
    def __init__(self, width=0, height=0):
        """Constructor function.

        Note: raise exceptions if size is not int.

        Args:
            width (int): The width from the user.
            height (int): The height from the user.
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    
    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of __width.

        Args:
            value (int): value of __width.

        Raises:
            ValueError: if < 0.
            TypeError: if not int.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the value of __height.

        Args:
            value (int): value of __height.

        Raises:
            ValueError: if < 0.
            TypeError: if not int.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
