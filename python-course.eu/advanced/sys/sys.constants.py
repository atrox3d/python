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
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	) #
log=logging.getLogger(__name__)

format = "sys.%-{0}.{0}s = %s".format(20)
if __name__ == "__main__":
	for item in [x for x in dir(sys) if not x.startswith("__") or x.startswith("__std") ]:
		log.info(format, item, getattr(sys, item))
		#print(item)
		