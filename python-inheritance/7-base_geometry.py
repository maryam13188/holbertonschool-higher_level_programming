#!/usr/bin/python3
"""
7-base_geometry module
Defines a BaseGeometry class with:
- area() method that raises Exception
- integer_validator() method to validate integer values > 0
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer > 0.

        Args:
            name (str): Name of the variable
            value: Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
