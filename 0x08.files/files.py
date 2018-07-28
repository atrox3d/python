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
#	using literal string interpolation (f-strings) to create variable width format
#
width=50
format=f'%-{width}.{width}s : %s'
