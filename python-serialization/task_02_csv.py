#!/usr/bin/python3
"""Module to convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file named data.json.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        data = []

        with open(csv_filename, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError):
        return False
