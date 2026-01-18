#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Return list of True/False for numbers divisible by 2."""
    return [x % 2 == 0 for x in my_list]
