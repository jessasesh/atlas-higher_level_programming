#!/usr/bin/python3
"""
Function that divides element by element 2 lists
"""
def list_division(my_list_1, my_list_2, list_length):
    # Initializes an empty list to store division reaults
    n_list = []
    # Iterates up to specified list_length
    for i in range(list_length):
        try:
            # Attempt to perform division for the corresponding
            # elements in the lists
            quotient = my_list_1[i] / my_list_2[i]
        # Handle errors
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            quotient = 0
        except IndexError:
            print("{}".format("out of range"))
            quotient = 0
        finally:
            # Append the quptient to new list
            n_list.append(quotient)
    # Return the list containing results
    return n_list
