#!/usr/bin/env python3

#
#	import regex package
#
import re
#
#	create regex object
#
#	r'string' : raw string (no escape interpretation, otherwise \\d)
#
phoneNumberRegex =  re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
#
#	search text against regex
#
mo = phoneNumberRegex.search('My number is 415-555-4242.')
#
#	two different string interpolation methods
#
print("mo.group    %s" % mo.group())
print("mo.group    {}".format(mo.group()))
#
#	print tuple
#
print("mo.groups   {}".format(mo.groups()))
#
#	play with tuple
#
for group in mo.groups():
	print("mo.group    %5.5s" % group)
#
#	play with string format
#
for i in range(len(mo.groups())+1):
	print("group %d	%20.20s" % (i, mo.group(i)))
	print("group {}	{:>20s}".format( i, mo.group(i)))
#
# multi assignment
#
a, b, c = mo.groups()
print( "a={}, b={}, c={}".format( a, b, c ))
#
#	print result
#
print('\nPhone number found: ' + mo.group())
