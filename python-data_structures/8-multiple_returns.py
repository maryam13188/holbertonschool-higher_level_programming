#!/usr/bin/python3

def multiple_returns(sentence):
    """Return tuple with length and first character of string."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
