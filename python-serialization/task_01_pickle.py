#!/usr/bin/python3
"""Module for serializing and deserializing a custom object using pickle."""

import pickle


class CustomObject:
    """CustomObject class that supports pickling."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file.

        Args:
            filename (str): File to save the object to.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Args:
            filename (str): File to load the object from.

        Returns:
            CustomObject or None
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError):
            return None
