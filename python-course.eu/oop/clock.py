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
		log.debug("%-10.10s = %s", 'hours', hours)
		log.debug("%-10.10s = %s", 'minutes', minutes)
		log.debug("%-10.10s = %s", 'seconds', seconds)
		self.setclock(hours, minutes, seconds)

	def setclock(self, hours, minutes, seconds):
		"""
		"""
		log.debug("%-10.10s = %s", 'hours', hours)
		log.debug("%-10.10s = %s", 'minutes', minutes)
		log.debug("%-10.10s = %s", 'seconds', seconds)
		
	def __str__(self):
		log.debug("%-10.10s = %s", '__str__', '__str__')
		
	def tick(self):
		log.debug("%-10.10s = %s", 'tick', 'tick')

if __name__ == "__main__":
	pass