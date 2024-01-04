#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_numb = abs(number) % 10
if number < 0:
    l_numb = -l_numb
print(f"Last digit of {number} is {l_numb} and is ", end="")
if l_numb > 5:
    print("greater than 5")
elif l_numb == 0:
    print("0")
else:
    print("less than 6 and not 0")
