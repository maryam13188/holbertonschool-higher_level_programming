#!/usr/bin/python3
"""
1-my_list module
Defines a class MyList that inherits from list and has a
public method to print the list sorted.
"""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))
