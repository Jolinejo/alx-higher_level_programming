#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""


class BaseGeometry:
    """An empty class the defines BaseGeometry.
    """
    def area(self):
        """A func that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a func that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
