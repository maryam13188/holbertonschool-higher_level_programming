#!/usr/bin/python3
"""Module that defines a Student class with JSON
serialization and deserialization.
"""


class Student:
    """Student class with public attributes and JSON methods."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.
        If attrs is a list, only selected attributes are returned.
        """
        if isinstance(attrs, list):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
