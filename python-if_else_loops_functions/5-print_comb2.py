#!/usr/bin/python3
# Prints numbers from 0 to 99
for num in range(100):
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
