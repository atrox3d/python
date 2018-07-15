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

sys.path.append("..") # Adds higher directory to python modules path
from lib.fakepyperclip import fakepyperclip as pyperclip

text = pyperclip.paste()
if text != None:
	log.info("ok")
else:
	log.fatal("something went wrong, exiting")
	sys.exit(1)

