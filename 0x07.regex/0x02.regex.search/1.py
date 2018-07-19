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
phoneNumberRegex =  re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#
#	search text against regex
#
mo = phoneNumberRegex.search('My number is 415-555-4242.')
#
#	print result
#
print('Phone number found: ' + mo.group())
