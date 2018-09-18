#!env python3

import sys

from xml.etree import ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

