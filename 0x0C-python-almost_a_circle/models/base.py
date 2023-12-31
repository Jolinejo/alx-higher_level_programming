#!/usr/bin/python3
"""
Base
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json conv"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json rep to file"""
        list_dict = []
        try:
            for inst in list_objs:
                list_dict.append(inst.to_dictionary())
        except Exception:
            pass
        data = cls.to_json_string(list_dict)
        filename = cls.__name__ + ".json"
        with open(filename, 'w+') as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """from json to list"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create from dict"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """create list from json_str"""
        json_str = ""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                json_str = f.read()
        except Exception:
            return []
        list_dict = cls.from_json_string(json_str)
        list_inst = []
        for item in list_dict:
            list_inst.append(cls.create(**item))
        return list_inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """turtle python"""
        import turtle
        turtle.Turtle()

        list_rec = ["DarkMagenta", "MediumPurple", "plum"]
        list_sq = ["OrangeRed4", "tomato", "salmon"]

        i = 0
        for rect in list_rectangles:
            turtle.fillcolor(list_rec[i])
            turtle.begin_fill()
            for j in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            i += 1
            turtle.end_fill()

        i = 0
        for squ in list_squares:
            turtle.fillcolor(list_sq[i])
            turtle.begin_fill()
            for j in range(4):
                turtle.forward(squ.width)
                turtle.right(90)
            i += 1
            turtle.end_fill()
        turtle.end()
