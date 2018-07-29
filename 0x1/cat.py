#!/usr/bin/env python3
import sys

if '-n' in sys.argv[1:]:
	lines=True
else:
	lines=False

linenumber=0
try:
	for line in sys.stdin:
		linenumber+=1
		if lines:
			print("%d %s" % (linenumber, line.rstrip()))
		else:
			print(line.rstrip())
except KeyboardInterrupt:
	sys.exit()
	
