#!/usr/bin/python3
"""Module for serializing and deserializing dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Name of the XML file to save data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Name of the XML file to read data from.

    Returns:
        dict: Deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
