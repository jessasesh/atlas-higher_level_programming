#!/usr/bin/python3
"""
Write class to manage id attribute in all
future classes and to avoid duplicating
the same code.
"""
import json


class Base:
    """
    Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
         Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json string representation.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes json string to a file.
        """
        if list_objs is None:
            list_objs = []

        json_list = []
        for obj in list_objs:
            obj_dict = {}
            for key, value in obj.__dict__.items():
                if not key.startswwith(" "):
                    obj_dict[key] = value
            json_list.append(obj_dict)

        json_string = cls.to_json_string(json_list)
        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            file.write(json_string)
