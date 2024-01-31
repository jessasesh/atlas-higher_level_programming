#!/usr/bin/python3
"""
This function reads a text file and
prints it to stdout.
"""


def read_file(filename=""):
    """
    Opens, reads, and prints text file
    to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
