#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    
    #Calculates number of command-line arguments
    arg_count = len(sys.argv) - 1
    
       #Checks the number of arguments and prints
       #required messages
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))
    
    # Prints the list of arguments
    for i in range(arg_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
