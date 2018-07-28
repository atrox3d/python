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
log.info("current working directory : %s", pwd)
log.info("filename                  : %s", sys.argv[0])
