#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON representation.
"""


class Student:
    """Student class with first_name, last_name, age,
    and JSON representation.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name,
        and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.
        If attrs is a list, only attributes in this list are included.
        """
        if isinstance(attrs, list):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__.copy()
