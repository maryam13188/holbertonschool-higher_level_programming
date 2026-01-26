#!/usr/bin/python3
"""
6-base_geometry module
Defines a BaseGeometry class with a method area() that raises
an exception when called.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
