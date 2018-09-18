#!env python3

import sys

from xml.etree import ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

#print('root', root)
#print('root public members  : ', list([ p for p in dir(root) if not p.startswith('__')]))
#print('root private members : ', dir(root))
#print(root.__getitem__(0))

# one specific item attribute
print('item #2 attribute')
print(root[0][1].attrib)

