#!/usr/bin/python3
"""
test_rectangle
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


class test_rectangle(unittest.TestCase):
    """class for testing the rectangle"""

    def test_inhert(self):
        """test inhertiance"""
        self.assertTrue(isinstance(Rectangle(1, 2), Base))
        
    def test_Instance(self):
        """testing the instance"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r1.width = 1
        r1.height = 1
        r1.x = 1
        r1.y = 1
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)

    def test_Errors(self):
        """testing invalid values"""
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "10", 1)
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 10, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1)
        with self.assertRaises(TypeError):
            r2.width = "10"
        with self.assertRaises(TypeError):
            r2.height = "10"
        with self.assertRaises(TypeError):
            r2.x = "10"
        with self.assertRaises(TypeError):
            r2.y = "10"
        with self.assertRaises(ValueError):
            r2.width = 0
        with self.assertRaises(ValueError):
            r2.height = 0
        with self.assertRaises(ValueError):
            r2.width = -1
        with self.assertRaises(ValueError):
            r2.height = -1
        with self.assertRaises(ValueError):
            r2.x = -1
        with self.assertRaises(ValueError):
            r2.y = -1

    def test_Area(self):
        """testing area"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """testing disp"""
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)
        output = io.StringIO()
        sys.stdout = output
        dis1 = "####\n####\n####\n####\n####\n####\n"
        dis2 = "##\n##\n"
        r1.display()
        self.assertEqual(dis1, output.getvalue())
        output.seek(0)
        output.truncate(0)
        r2.display()
        self.assertEqual(dis2, output.getvalue())
        output.seek(0)
        output.truncate(0)
        r1 = Rectangle(2, 3, 2, 2)
        r2 = Rectangle(3, 2, 1, 0)
        dis1 = "\n\n  ##\n  ##\n  ##\n"
        dis2 = " ###\n ###\n"
        r1.display()
        self.assertEqual(dis1, output.getvalue())
        output.seek(0)
        output.truncate(0)
        r2.display()
        self.assertEqual(dis2, output.getvalue())
        sys.stdout = sys.__stdout__

    def test_str(self):
        """testing str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        r1str = "[Rectangle] (12) 2/1 - 4/6"
        r2str = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r1), r1str)
        self.assertEqual(str(r2), r2str)

    def test_updateargs(self):
        """testing update args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1str = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(str(r1), r1str)
        r1.update(89)
        r1str = "[Rectangle] (89) 10/10 - 10/10"
        r1.update(89, 2)
        r1str = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r1), r1str)
        r1.update(89, 2, 3)
        r1str = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r1), r1str)
        r1.update(89, 2, 3, 4)
        r1str = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r1), r1str)
        r1.update(89, 2, 3, 4, 5)
        r1str = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r1), r1str)

    def test_updatekwargs(self):
        """testing update kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        r1str = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(r1), r1str)
        r1.update(width=1, x=2)
        r1str = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(str(r1), r1str)
        r1.update(y=1, width=2, x=3, id=89)
        r1str = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(r1), r1str)
        r1.update(x=1, height=2, y=3, width=4, kilogram=5)
        r1str = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(r1), r1str)
        self.assertFalse(hasattr(r1, "kilogram"))
        r1.update(5, 6, 7, 8, 9, height=1, width=2, y=5, x=4)
        r1str = "[Rectangle] (5) 8/9 - 6/7"
        self.assertEqual(str(r1), r1str)
        r1.update(8, height=1, width=2, y=5, x=4)
        r1str = "[Rectangle] (8) 8/9 - 6/7"
        self.assertEqual(str(r1), r1str)

    def test_ToDictionary(self):
        """testing dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r1_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertTrue(type(r1_dictionary) is dict)
        self.assertDictEqual(r1_dictionary, r1_dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2str = "[Rectangle] (1) 1/9 - 10/2"
        self.assertEqual(str(r2), r2str)
        self.assertNotEqual(r1, r2)

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
