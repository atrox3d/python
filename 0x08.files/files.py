#!/usr/bin/env python3
import os, sys
import logging
#
#	logger configuration
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
#	get a logger
#
log=logging.getLogger(__name__) 
#
#	using literal string interpolation (f-strings) to create variable width format
#
width=20
format=f'%-{width}.{width}s : %s'
#
# let's open ourselves
#
scriptname=sys.argv[0]
thisfile=open(scriptname)
log.info(format, "scriptname", scriptname)

filecontent=thisfile.read()
print(filecontent)

thisfile.seek(0)
filelines=thisfile.readlines()
print(filelines)

thisfile.seek(0)
for line in thisfile:
	log.info(format, os.path.basename(scriptname), line.rstrip())
#
#
#
anotherfile=open("anotherfile", 'w')
anotherfile.write("write and close\n")
anotherfile.close()

anotherfile=open("anotherfile", 'a')
anotherfile.write("append and close\n")
anotherfile.close()

anotherfile=open("anotherfile")
for line in anotherfile:
	log.info(format, os.path.basename(anotherfile.name), line.rstrip())
	