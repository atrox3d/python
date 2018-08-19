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
		"""
		returns a string representing the clock value with the format "hh:mm:ss"
		"""
		value = "{:02d}:{:02d}:{:02d}".format(
												self._hours,
												self._minutes,
												self._seconds
											)
		log.debug("%-10.10s = %s", '__str__', value)
		return value
		
	def tick(self):
		"""
		increments the clock value
		"""
		if self._seconds == 59:
			self._seconds = 0
			if self._minutes == 59:
				self._minutes = 0
				if self._hours == 23:
					self._hours = 0
				else:
					self._hours += 1
			else:
				self._minutes += 1
		else:
			self._seconds += 1
		
		log.debug("%-10.10s = %s", 'tick', self.__str__())
		return self.__str__()

if __name__ == "__main__":
	c = Clock(22, 59, 58)
	log.info(c)
	c.tick()
	c.tick()
	c.tick()
	