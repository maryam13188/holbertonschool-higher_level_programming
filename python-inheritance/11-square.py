#!/usr/bin/python3
"""
11-square module
Defines a Square class that inherits from Rectangle (9-rectangle)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square

        Raises:
            TypeError, ValueError: If size is invalid
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the informal string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
