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
width=50
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
#
#	absolute path
#
abspath=os.path.abspath(sys.argv[0])
log.info(format, "absolute script path", abspath)
#
#	split
#
path, scriptname = os.path.split(abspath)
log.info(format, "absolute script path", path)
log.info(format, "script name", scriptname)
#
#	let's gather some stats
#
path='..'
for filename in os.listdir(path):
	currfile=os.path.abspath(os.path.join(path, filename))
	if os.path.exists(currfile):
		if os.path.isdir(currfile):
			log.info("%-*.*s : %s", width, width, currfile, "DIR")
		else
			currsize=os.path.getsize(currfile)
			log.info("%-*.*s : %d", width, width, currfile, currsize)
	else
		log.error(format, "path non found", currfile)
	
	

	


