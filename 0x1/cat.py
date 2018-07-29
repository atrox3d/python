#!/usr/bin/env python3
import sys
try:
	for line in sys.stdin:
		print(line.rstrip())
except KeyboardInterrupt:
	sys.exit()
	
