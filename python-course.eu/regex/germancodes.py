#!/usr/bin/env python3
""" https://www.python-course.eu/python3_re.php """
import re
from urllib.request import urlopen

url='https://www.python-course.eu/post_codes_germany.txt'

with urlopen(url) as gc:						# 	open online resource
	charset=gc.info().get_content_charset()     #	get charset
	for line in gc:                             #	loop over content
		print(line.decode(charset).rstrip())    #	decode every line
