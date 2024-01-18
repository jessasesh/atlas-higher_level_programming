#!/usr/bin/python3
"""
Safely prints the first "x" integers from "my_list"
"""
def safe_print_list_integers(my_list=[], x=0):
    
    # Initializes the count of printed integers
    count = 0
    
    # Iterate through the firt "x" elements of "my list"
    for i in range(x):
        try:
            # Attempt to print the integer
            print("{:d}".format(my_list[i]), end="")
            
            # Increment the count of successfully printed integers
            count += 1
        except (ValueError, TypeError):
            
            # Ignore ValueError and TypeError exceptions
            pass
    # Print a newline character to separate the output
    print()
    
    # Return the count of successfully printed integers
    return (count)
