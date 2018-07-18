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
if len(sys.argv) > 1:
	# from cli
	log.debug("argv's len: %s", len(sys.argv))
	log.debug(sys.argv)
	
	lines=sys.argv[1:]
	log.debug(lines)
	pyperclip.copy('\n'.join(lines))
else:
	# default
	pyperclip.copy('Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars')

##############################



text = pyperclip.paste()
if text != None:
	log.info("ok")
else:
	log.fatal("something went wrong, exiting")
	sys.exit(1)

