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
				"%(module)s | " + 
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
		pass
	

if __name__ == "__main__":
	pass