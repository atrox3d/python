#!/usr/bin/env python3
"""
	class simulating a clock
"""

import logging
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				"%(module)s | " + 
				"%(name)-10s:" +
				"%(funcName)-10s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S'
	) #
log=logging.getLogger(__name__)
#
#
#
class Clock(object):
	def __init__(self, hours, minutes, seconds):
		"""
		"""
		self.setclock(self, hours, minutes, seconds)

	def setclock(self, hours, minutes, seconds):
		"""
		"""
		pass
		
	def __str__(self):
		pass

if __name__ == "__main__":
	pass