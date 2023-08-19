#!/usr/bin/python3
"""
rectangle
"""
from models.base import Base


class Rectangle(Base):
    """A class the defines a rectangle.

    Args:
        width(int): The width of the square.
        height(int): The height of the square.

    Attributes:
        __width: Private attribute width.
        __height: Private attribute height.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor func"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter for width"""
        self.__width = val

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter for heigt"""
        self.__height = val

    @property
    def x(self):
        """getter for x"""
        return self.__x
    
    @x.setter
    def x(self, val):
        """setter for width"""
        self.__x = val

    @property
    def y(self):
        """getter for width"""
        return self.__y
    
    @y.setter
    def y(self, val):
        """setter for width"""
        self.__y = val
