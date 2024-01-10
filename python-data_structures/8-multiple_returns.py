#!/usr/bin/python3
# Function that returns a tuple with a few extras

def multiple_returns(sentence):

    if sentence == "":
        return 0, None
    else:
        return len(sentence), sentence[0]
