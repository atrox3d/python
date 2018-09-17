#!env python3
from xml.dom import minidom

datasource = open('items.xml')
mydoc = minidom.parse(datasource)

items = mydoc.getElementsByTagName('item')

print('\nitem #2 attribute')
print(items[1].attributes['name'].value)

print('\nAll attributes:')  
for elem in items:
	print(elem.attributes['name'].value)
	#print(dir(elem))
		
print('\nItem #2 data')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

print('\nAll item data:')  
for elem in items:
	print(elem.firstChild.data)
	

