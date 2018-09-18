#!env python3

import sys

from xml.etree import ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# one specific item attribute
print('item #2 attribute')
print(root[0][1].attrib)

