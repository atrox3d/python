#!/usr/bin/env python3
#
# BulletpointAdder.py - adds wikipedia bullet points to each line
#
import sys

import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	#format="[%(asctime)s][%(module)s][%(name)s][%(levelname)-6s] - %(message)s",
	format="%(asctime)s %(module)-20s %(levelname)-10s : %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
log=logging.getLogger(__name__)

# using a symbolic link to ../lib now
#sys.path.append("..") # Adds higher directory to python modules path
from lib.fakepyperclip import fakepyperclip as pyperclip

##############################
# simulate external copy
##############################
#
# check if we have arguments from CLI
#
if len(sys.argv) > 1:
	#
	# we have arguments, let's check them out and print them
	#
	log.debug("argv's len: %s", len(sys.argv))
	log.debug("argv      : %s", sys.argv)
	#
	# get lines as arguments from cli starting from 1
	#
	lines=sys.argv[1:]
	log.debug("lines     : %s",lines)
	#
	# join arguments with newline
	#
	pyperclip.copy('\n'.join(lines))
else:
	#
	# default:
	#
	pyperclip.copy('Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars')
##############################
# /simulate external copy
##############################

#
# get the "copied" text
#
text = pyperclip.paste()
#
# check if we have something
#
if text != None:
	log.info("ok")
	#
	# ok, we have data
	#
else:
	#
	# no data from clipboard, exit
	#
	log.fatal("something went wrong, no data found in clipboard. exiting")
	sys.exit(1)

