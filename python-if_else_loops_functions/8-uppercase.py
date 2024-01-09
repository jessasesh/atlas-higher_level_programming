#!/usr/bin/python3
# Prints a string in uppercase
def uppercase(str):
    uppercase_char = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
    print(uppercase_char, end="")
    print("")
