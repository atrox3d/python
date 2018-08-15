#!/usr/bin/env python3
import logging
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	"%(asctime)s | " + 
				"%(module)-15s | " + 
				"%(name)-10s:%(funcName)-20s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S'
	) #
log=logging.getLogger(__name__)
#
#
#
class Robot:
	pass

if __name__ == "__main__":
	r = Robot()

