#!/usr/bin/python3
"""
Program that prints all the names defined by
the compiled module hidden_4.pyc
"""
import hidden_4

if __name__ == "__main__":

    # Loop that iterates over member within
    # hidden_4 module
    for member_name in dir(hidden_4):
        # Checks if member is not hidden
        if member_name[0] != "_":
            # Prints the name of member
            print(member_name)
