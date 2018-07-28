#!/usr/bin/env python3
import os, sys
import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
log=logging.getLogger(__name__) 

pwd = os.getcwd()
width=25
log.info("%-*.*s : %s", width, width, "current working directory", pwd)
log.info("%-*.*s : %s", width, width, "filename", sys.argv[0])

os.chdir(pwd)
log.info("%-*.*s : %s", width, width, "current working directory", pwd)

relpath=os.path.relpath(pwd)
log.info("%-*.*s : %s", width, width, "relative working directory", relpath)
