#!/usr/bin/python3
"""
This module contains the MyList class which inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list with additional sorting functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying
        the original list.
        """
        print(sorted(self))
