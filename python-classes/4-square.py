#!/usr/bin/python3
"""Defines a Square class with controlled access to size."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
