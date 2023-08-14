#!/usr/bin/python3
"""A module that contains the definition for an empty class
"""


class MyInt(int):
    """Rebel int class"""
    def __eq__(self, other):
        """equal operator."""
        return self != other

    def __ne__(self, other):
        """not equal operator."""
        return self == other
