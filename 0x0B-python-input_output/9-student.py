#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""


class Student:
    """A class the defines a student.

    Attributes:
        first_name(str): public
        last_name(str): public
        age(int): public
    """
    def __init__(self, first_name, last_name, age):
        """constructir func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
