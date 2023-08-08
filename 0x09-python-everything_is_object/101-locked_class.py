#!/usr/bin/python3
"""A module that contains a locked class.

"""


class LockedClass():
    """A locked Class.

    Attributes:
        first_name: only attr
    """
    __slots__ = ['first_name']
