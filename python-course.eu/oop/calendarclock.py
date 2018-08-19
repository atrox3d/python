#!/usr/bin/env python3
"""
class simulating a calendar
"""

import logging
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

from clock import Clock
from calendar import Calendar
#
#
#
class CalendarClock(Clock, Calendar):
	
	def __init__(
		self,
		day,
		month,
		year,
		hours,
		minutes,
		seconds
	):
		#
		#	play with args : get list of arg keys in reverse order except self
		#
		args = [ arg for arg in list(locals().keys())[::-1] if  not arg == 'self' ]
		for arg in args:
			log.debug("%-10.10s = %s", arg, locals()[arg])
		
		Clock.__init__( self, hours, minutes, seconds )
		Calendar.__init__( self, day, month, year )
	
	def __str__(self):
		value = Calendar.__str__(self) + ", " + Clock.__str__(self)
		return value

if __name__ == "__main__":
	cc = CalendarClock(1,2,3000,4,5,6)
	print(cc)