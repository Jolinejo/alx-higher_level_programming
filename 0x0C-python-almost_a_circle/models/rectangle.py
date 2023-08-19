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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter for width"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter for heigt"""
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter for x"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter for y"""
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """return rec area"""
        ar = self.__width * self.__height
        return ar

    def display(self):
        """prints the square.

        Note: if __size is 0 print an empty line.
        """
        for v in range(self.__y):
            print("")
        for i in range(1, self.__height+1):
            for k in range(self.__x):
                print(" ", end='')
            for j in range(0, self.__width):
                print("#", end='')
            print("")

    def update(self, *args, **kwargs):
        """updating using args"""
        atrr_lis = ["id",
                    "_Rectangle__width", "_Rectangle__height",
                    "_Rectangle__x", "_Rectangle__y"
                    ]
        i = 0
        for arg in args:
            if i == len(atrr_lis):
                break
            setattr(self, atrr_lis[i], arg)
            i += 1
        if i == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict rep"""
        return {'x': self.__x, 'y': self.__y,
                'id': self.id, 'height': self.__height, 'width': self.__width}

    def __str__(self):
        """str represintation"""
        s = "[" + str(self.__class__.__name__) + "] ("
        s += str(self.id) + ") " + str(self.__x) + "/" + str(self.__y)
        s += " - "
        if str(self.__class__.__name__) == "Rectangle":
            s += str(self.__width) + "/" + str(self.__height)
        else:
            s += str(self.__width)
        return s
