#!/usr/bin/python3
"""
test_base
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import pathlib as pl


class test_base(unittest.TestCase):
    """class for testing the base"""

    def test_ID(self):
        """testing the id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_ToJsonString(self):
        """to json testing"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary2 = Base.to_json_string([])
        json_dictionary3 = Base.to_json_string(None)
        from_js_dict = json.loads(json_dictionary)
        self.assertTrue(type(json_dictionary) is str)
        self.assertDictEqual(from_js_dict[0], dictionary)
        self.assertEqual(json_dictionary2, "[]")
        self.assertEqual(json_dictionary3, "[]")

    def test_SaveToFile(self):
        """file saving tests"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        path = pl.Path("Rectangle.json")
        assert path.is_file()
        list_dict = list()
        with open("Rectangle.json", "r") as f:
            list_dict = json.load(f)
        self.assertDictEqual(list_dict[0], r1.to_dictionary())
        self.assertDictEqual(list_dict[1], r2.to_dictionary())
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            list_dict = json.load(f)
        self.assertEqual(list_dict, [])
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            list_dict = json.load(f)
        self.assertEqual(list_dict, [])

    def test_FromJsonString(self):
        """check list of json rep"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_output, list_input)
        json_list_input = Rectangle.to_json_string([])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_Create(self):
        """test create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_LoadFromFile(self):
        """test creating from file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_i = [r1, r2]
        Rectangle.save_to_file(list_rect_i)
        list_rectangles_o = Rectangle.load_from_file()
        for i in range(2):
            self.assertEqual(str(list_rect_i[i]), str(list_rectangles_o[i]))
            self.assertNotEqual(list_rect_i[i], list_rectangles_o[i])
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_i = [s1, s2]
        Square.save_to_file(list_squares_i)
        list_squares_o = Square.load_from_file()
        for i in range(2):
            self.assertEqual(str(list_squares_i[i]), str(list_squares_o[i]))
            self.assertNotEqual(list_squares_i[i], list_squares_o[i])

    def test_loadfromFileError(self):
        """a file doesn't exist"""
        list_rectangles_o = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_o, [])
        list_squares_o = Square.load_from_file()
        self.assertEqual(list_squares_o, [])

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
