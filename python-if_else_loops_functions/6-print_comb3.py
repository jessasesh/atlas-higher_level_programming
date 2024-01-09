#!/usr/bin/python3
#Prints all possible different combinations of two digits

for tens in range(10):
    for ones in range(tens, + 1, 10):
        f = ("{:02d}".format(tens * 10 + ones)
        print(f, end=", ")
