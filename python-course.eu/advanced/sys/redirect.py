#!/usr/bin/env python3
"""

"""

import logging, sys
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				"%(module)-15.15s | " + 
				"%(name)-10s:" +
				"%(funcName)-15.15s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S'
	) #
log=logging.getLogger(__name__)

if __name__ == "__main__":
	for stream in [ sys.stdin, sys.stdout, sys.stderr ]:
		log.info("stream name: %s", stream.name)
		log.info("stream     : %s", stream)
		#for item in dir(stream):
		#	log.info("dir stream : %s", item)
		