#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """A class for unit testing the max_integer

    Is a subclass of the unittest TestCase
    """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-2, -1, -3]), -1)
        self.assertEqual(max_integer([1]), 1)
