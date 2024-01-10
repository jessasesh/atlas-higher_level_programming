#!/usr/bin/python3
'''
Function that takes a 2D matrix as an argument
with a default value of an empty list containing 
an empty list; prints a matrix of integers
'''
def print_matrix_integer(matrix=[[]]):
    
    # Outer loop iterating each row
    for c_row in range(len(matrix)):
        
        # Inner loop iterating through each element in current row
        for c_element in range(len(matrix[c_row])):
            
            # If the current element is in last row
            if c_element == len(matrix[c_row]) - 1:
                
                # Print the formatted element without a space
                print("{:d}".format(matrix[c_row][j]), end='')
            
            # If current element is not in last row
            else:
                
                # Prints formatted element with a space
                print("{:d}".format(matrix[c_row][c_element]), end=' ')
        # Prints newline character
        print()
