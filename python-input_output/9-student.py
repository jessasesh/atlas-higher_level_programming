#!/usr/bin/python3
"""
Write a class with instance retrieval.
"""


class Student:
    """
    Representation of a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves dictionary of student and attributes.
        """
        return self.__dict__
