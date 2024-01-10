#!/usr/bin/python3
# Function that prints the numbers from 1 to 100

def fizzbuzz():

    # Iterates through numbers
    for number in range(1, 101):

        # If number is divisible by both 3 and 5
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        
        # If number is divisible by 3
        elif number % 3 == 0:
            print("Fizz ", end="")
        
        # If number is divisible by 5
        elif number % 5 == 0:
            print("Buzz ", end="")
        
        # If number isn't divisible by either 3 nor 5
        else:
            print("{} ".format(number), end="")
