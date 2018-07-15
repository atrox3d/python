#!/usr/bin/env python3
import logging
import sys
from pathlib import Path 

# just to try the complete syntax
from fakepyperclip import fakepyperclip as pyperclip

logging.basicConfig(
    #filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
	datefmt='[%Y/%m/%d|%H:%M:%S]'
    )

# log-like
#print("[{}] first test".format(Path(sys.argv[0]).name))
logging.debug("[{}] first test".format(Path(sys.argv[0]).name))
info("hello")
#help(pyperclip)
logging.debug(pyperclip.__doc__)

pyperclip.copy("hello")
pyperc