#!/usr/bin/env python3
import logging
import sys
from pathlib import Path 

# just to try the complete syntax
from fakepyperclip import fakepyperclip as pyperclip

logging.basicConfig(
    #filename="test.log",
    level=logging.DEBUG,
    #format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
    format="[%(asctime)s][%(module)s][%(name)s][%(levelname)-6s] - %(message)s",
	datefmt='%Y/%m/%d|%H:%M:%S'
    )

log=logging.getLogger("main")


# log-like
#print("[{}] first test".format(Path(sys.argv[0]).name))
#log.debug("[{}] first test".format(Path(sys.argv[0]).name))
log.info("first test")
log.info("hello")
#help(pyperclip)
for line in pyperclip.__doc__.split('\n'):
	log.debug(line)

log.debug('pyperclip.copy("hello")')
pyperclip.copy("hello")
log.debug('pyperclip.paste()')
pyperclip.paste()

