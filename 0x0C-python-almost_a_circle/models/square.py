#!/usr/bin/python3
"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class the defines a rectangle.

    Args:
        width(int): The width of the square.
        height(int): The height of the square.

    Attributes:
        __width: Private attribute width.
        __height: Private attribute height.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, val):
        """size setter"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """updating using args"""
        atrr_lis = ["id",
                    "width", "height",
                    "x", "y"
                    ]
        i = 0
        for arg in args:
            if i == len(atrr_lis):
                break
            if i == 1:
                setattr(self, atrr_lis[i], arg)
                setattr(self, atrr_lis[2], arg)
                i += 1
            else:
                setattr(self, atrr_lis[i], arg)
            i += 1
        if i == 0:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                elif hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """dict rep"""
        return {'x': self.x, 'y': self.y,
                'id': self.id, 'size': self.height}
