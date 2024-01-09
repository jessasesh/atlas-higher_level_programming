#!/usr/bin/python3
#Prints all possible different combinations of two digits

for z in range(10):
    for x in range(10):
        if z < x:
            if z == 8 and x == 9:
                print("{}{}".format(z, x))
            else:
                print("{}{}, ".format(z, x), end="")
