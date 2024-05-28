#!/usr/bin/python3
"""
Function that reads a text file and prints.
"""
def read_file(filename=""):
    """
    Reads a file and prints contents to standard output.
    """
    with open(filename, encoding="UTF-8") as file:
        content = file.read()
        print(content, end="")
