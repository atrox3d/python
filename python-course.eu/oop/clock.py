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
		0 < hours   < 24
		0 < minutes < 60
		0 < seconds < 60
		"""
		log.debug("%-10.10s = %s", 'hours', hours)
		log.debug("%-10.10s = %s", 'minutes', minutes)
		log.debug("%-10.10s = %s", 'seconds', seconds)
		self.setclock(hours, minutes, seconds)

	def setclock(self, hours, minutes, seconds):
		"""
		0 < hours   < 24
		0 < minutes < 60
		0 < seconds < 60
		"""
		log.debug("%-10.10s = %s", 'hours', hours)
		log.debug("%-10.10s = %s", 'minutes', minutes)
		log.debug("%-10.10s = %s", 'seconds', seconds)
		
		if type(hours) == int and 0 <= hours and hours < 24:
			self._hours = hours
		else:
			raise TypeError("0 < hours < 24")
			
		if type(minutes) == int and 0 <= minutes and minutes < 60:
			self._minutes = minutes
		else:
			raise TypeError("0 < minutes < 60")
			
		if type(seconds) == int and 0 <= seconds and seconds < 60:
			self._seconds = seconds
		else:
			raise TypeError("0 < seconds < 60")
			
		
		
	def __str__(self):
		log.debug("%-10.10s = %s", '__str__', '__str__')
		return "__str__"
		
	def tick(self):
		log.debug("%-10.10s = %s", 'tick', 'tick')

if __name__ == "__main__":
	c = Clock(22, 59, 30)
	print(c)
	c.tick()
	