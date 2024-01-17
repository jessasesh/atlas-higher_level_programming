#!/usr/bin/python3

import sys
"""Program that prints the reulut of the addition
   of all arguments
"""

if __name__ == "__main__":
    
    #Total number of arguments
    num_args = len(sys.argv)

    #Total value of all arguments
    total = 0

    #Iterate through arguments, coverts each argument
    #into an integer, and then adds that to the total
    for x in range(1, num_args):
        total += int(sys.argv[x])
    
    #Prints the sum of all arguments
    print(total)
