#!env python3

import sys

from xml.dom import minidom

# get path to xml via args or use default
datafile = sys.argv[1] if len(sys.argv) > 1 else 'items.xml'

# open and parse datafile
datasource = open(datafile)
mydoc = minidom.parse(datasource)

# search item tags
items = mydoc.getElementsByTagName('item')

print('\nitem #2 attribute')
print(items[1].attributes['name'].value)

print('\nAll attributes:')  
for elem in items:
	print(elem.attributes['name'].value)
		
print('\nItem #2 data')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

print('\nAll item data:')  
for elem in items:
	print(elem.firstChild.data)
	

