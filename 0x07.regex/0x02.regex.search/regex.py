#!/usr/bin/env python3
import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
log=logging.getLogger(__name__) 
#
#	import regex package
#
import re
#
#	create regex object
#
#	r'string' : raw string (no escape interpretation, otherwise \\d)
#
regex = r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
log.debug("regex	: %s" % regex)
#
phoneNumberRegex =  re.compile(regex)
#print("phoneNumberRegex
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
#
#	keyword formatting
#
print( "a={}, b={}, c={c}".format( a, b, c=c ))
#
#	print result
#
print('\nPhone number found: ' + mo.group())
