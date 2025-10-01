#!/usr/bin/python3
"""This moudule explors serialization and deserialization
using XML as an alternative format to JSON"""

# The xml.etree.ElementTree module implements a simple
# and efficient API for parsing and creating XML data.
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize the dictionary into XML and save it to the given filename

        Args:
        dictionary: The dictionary to convert.
        filename: the destination file of xml.
    """
    # 1: creat root node - data: the contianer of XML
    root = ET.Element("data")

    for key, value in dictionary.items():
        # 2: create child node under root, the tagname is key from dict
        child = ET.SubElement(root, str(key))
        # 3: the context of child node is the value from dict
        child.text = str(value)

    # 4: Create a XML tree using root node
    tree = ET.ElementTree(root)

    # 5: Write the XML to filename
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Parse XML data into Python dictionary"""
    # 1: Parsing a XML tree from filename
    tree = ET.parse(filename)

    # 2: Getting the root <data>
    root = tree.getroot()

    # 3: Loop every child node under the root
    # make a child node to a python dict
    # child.tag = key in dict; child.text = value in dict
    pairs = [(child.tag, child.text) for child in root]
    result = dict(pairs)

    return result
