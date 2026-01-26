#!/usr/bin/python3
"""
9-rectangle module
Defines a Rectangle class that inherits from BaseGeometry (7-base_geometry)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError, ValueError: If width or height are invalid
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the informal string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
