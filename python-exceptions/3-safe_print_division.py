#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the quotient of a divided by b."""
    try:
        # Attempt to calculate quotient
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        
        # Handle TypeErrors
        quotient = None
    finally:
        # Print result of division
        print("Inside result: {}".format(quotient))
    # Return the calculated quotient, or None
    return (quotient)
