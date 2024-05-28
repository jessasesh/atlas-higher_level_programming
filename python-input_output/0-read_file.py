#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a file and prints contents to standard output.
    """
    with open(filename, encoding="UTF-8") as file:
        content = file.read()
        print(content, end="")
