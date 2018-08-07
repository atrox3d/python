#!/usr/bin/env python3
import re
from urllib.request import urlopen

with urlopen('https://www.python-course.eu/post_codes_germany.txt') as gc:
	charset=gc.info().get_content_charset()
	for line in gc:
		print(line.decode(charset).rstrip())
