#!/usr/bin/python3
# Function that computes a square value
def square_matrix_simple(matrix=[]):
    # Use a list comprehension to create new matrix with square value
    return ([list(map(lambda x: x * x, row)) for row in matrix])
