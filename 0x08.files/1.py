#!/usr/bin/env python3
import os, sys
import logging
#
#	logger configuration
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
#	get a logger
#
log=logging.getLogger(__name__) 
#
#	where are we?
#
pwd = os.getcwd()
#
#	using literal string interpolation (f-strings) to create variable width format
#
width=25
format=f'%-{width}.{width}s : %s'
#
#	some infos
#
log.info(format, "current working directory", pwd)
log.info(format, "filename", sys.argv[0])
#
#	cwd pwd
#
os.chdir(pwd)
log.info(format, "current working directory", pwd)
#
#	relative pwd
#
relpath=os.path.relpath(pwd)
log.info(format, "relative working directory", relpath)

