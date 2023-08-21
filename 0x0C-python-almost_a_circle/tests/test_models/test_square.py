#!/usr/bin/python3
"""
test_square
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import pathlib as pl
import io
import sys


class test_square(unittest.TestCase):
    """class for testing the square"""
    def test_xywidthheight(self):
        """testing inst"""
        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.x, 0)
        s1.width = 1
        s1.height = 1
        s1.x = 1
        s1.y = 1
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)
        with self.assertRaises(TypeError):
            s1.width = "10"
        with self.assertRaises(TypeError):
            s1.height = "10"
        with self.assertRaises(TypeError):
            s1.x = "10"
        with self.assertRaises(TypeError):
            s1.y = "10"
        with self.assertRaises(ValueError):
            s1.width = 0
        with self.assertRaises(ValueError):
            s1.height = 0
        with self.assertRaises(ValueError):
            s1.width = -1
        with self.assertRaises(ValueError):
            s1.height = -1
        with self.assertRaises(ValueError):
            s1.x = -1
        with self.assertRaises(ValueError):
            s1.y = -1
        self.assertRaises(TypeError, Square, "10")
        self.assertRaises(TypeError, Square, 1, "3")
        self.assertRaises(TypeError, Square, 10, 2, "4")
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, 1, 1, -1)

    def test_rectAttr(self):
        """for testing rect attr"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s1str = "[Square] (1) 0/0 - 5"
        s2str = "[Square] (2) 2/0 - 2"
        s3str = "[Square] (3) 1/3 - 3"
        self.assertEqual(str(s1), s1str)
        self.assertEqual(str(s2), s2str)
        self.assertEqual(str(s3), s3str)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        dis1 = "#####\n#####\n#####\n#####\n#####\n"
        dis2 = "  ##\n  ##\n"
        dis3 = "\n\n\n ###\n ###\n ###\n"
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        self.assertEqual(dis1, output.getvalue())
        output.seek(0)
        output.truncate(0)
        s2.display()
        self.assertEqual(dis2, output.getvalue())
        output.seek(0)
        output.truncate(0)
        s3.display()
        self.assertEqual(dis3, output.getvalue())
        sys.stdout = sys.__stdout__

    def test_size(self):
        """testing size setter and getter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_errors(self):
        """tessing errors"""
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "10"
        with self.assertRaises(ValueError):
            s1.size = 0
        with self.assertRaises(ValueError):
            s1.size = -1

    def test_update(self):
        """testing update"""
        s1 = Square(5)
        s1.update(10)
        s1str = "[Square] (10) 0/0 - 5"
        self.assertEqual(str(s1), s1str)
        s1.update(1, 2)
        s1str = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(s1), s1str)
        s1.update(1, 2, 3)
        s1str = "[Square] (1) 3/0 - 2"
        self.assertEqual(str(s1), s1str)
        s1.update(1, 2, 3, 4)
        s1str = "[Square] (1) 3/4 - 2"
        self.assertEqual(str(s1), s1str)
        s1.update(x=12)
        s1str = "[Square] (1) 12/4 - 2"
        self.assertEqual(str(s1), s1str)
        s1.update(size=7, y=1)
        s1str = "[Square] (1) 12/1 - 7"
        self.assertEqual(str(s1), s1str)
        s1.update(size=7, id=89, y=1, km=6)
        s1str = "[Square] (89) 12/1 - 7"
        self.assertEqual(str(s1), s1str)
        self.assertFalse(hasattr(s1, "km"))

    def test_dict(self):
        """test to dict"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s1_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertTrue(type(s1_dictionary) is dict)
        self.assertDictEqual(s1_dictionary, s1_dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2str = "[Square] (1) 2/1 - 10"
        self.assertEqual(str(s2), s2str)
        self.assertEqual(str(s2), str(s1))
        self.assertNotEqual(s1, s2)

    def tearDown(self):
        """tearDown to reset objects"""
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
