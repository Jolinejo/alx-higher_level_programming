#!/usr/bin/python3
"""
Base
"""

class Base:
    """Base Class

    Attributes:
        __nb_objects(int): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor func

        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

