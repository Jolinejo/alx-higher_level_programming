#!/usr/bin/python3
"""A module that conatins the class MYLIST"""


class MyList(list):
    """MyList class that inherits from list

    Attributes:
        all list attributes
    """
    def print_sorted(self):
        """prints the list but sorted"""
        sor = self[:]

        sor.sort()

        print(sor)
