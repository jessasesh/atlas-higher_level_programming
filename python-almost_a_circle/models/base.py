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
    def to_json_string(self, list_dictionaries):
        """
        Returns json string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
