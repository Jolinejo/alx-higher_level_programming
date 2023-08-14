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
