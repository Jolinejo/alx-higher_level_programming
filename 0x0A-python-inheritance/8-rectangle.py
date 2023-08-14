#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class the defines a rectangle.

    Args:
        width(int): The width of the square.
        height(int): The height of the square.

    Attributes:
        __width: Private attribute width.
        __height: Private attribute height.
    """
    def __init__(self, width, height):
        """Constructor function.

        Note: raise exceptions if size is not int.

        Args:
            width (int): The width from the user.
            height (int): The height from the user.
        """
        self.integer_validator("width", width)
        self.__wdith = width
        self.integer_validator("height", height)
        self.__height = height
