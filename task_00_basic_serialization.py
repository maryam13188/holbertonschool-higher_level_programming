#!/usr/bin/python3
"""Module for basic serialization and deserialization using JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The output JSON filename.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): The input JSON filename.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

