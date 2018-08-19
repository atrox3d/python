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
class Calendar(object):
	months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	datestyle = "british"
	
	@staticmethod
	def leapyear(year):
		"""
		"""
		if not year % 4 == 0: return False
		elif not year % 100 == 0: return False
		elif not year % 400 == 0: return False
		else: return True
	
	def __init__(self, day, month, year):
		"""
		"""
		log.debug("%-10.10s = %s", 'day', day)
		log.debug("%-10.10s = %s", 'month', month)
		log.debug("%-10.10s = %s", 'year', year)
		self.setcalendar(day, month, year)
		
	def setcalendar(self, day, month, year):
		"""
		"""
		log.debug("%-10.10s = %s", 'day', day)
		log.debug("%-10.10s = %s", 'month', month)
		log.debug("%-10.10s = %s", 'year', year)
		for check in [ day, month, year ]:
			if not type(check) == int:
				log.error("parameters must be integers")
				raise TypeError( "parameters must be integers")
		
		if year < 1000: 
			log.error("year must be a 4 digit number")
			raise Exception( "year must be a 4 digit number")
		
		self.__day = day
		self.__month = month
		self.__year = year
		
	def __str__(self):
		if Calendar.datestyle == "british":
			value = "{:02d}/{:02d}/{:04d}".format(
													self.__day,
													self.__month,
													self.__year
												)
		else:
			value = "{:02d}/{:02d}/{:04d}".format(
													self.__month,
													self.__day,
													self.__year
												)
		log.debug("%-10.10s = %s", 'value', value)
		return value
	

if __name__ == "__main__":
	try:
		c = Calendar( 1, "2", 3000 )
	except:
		pass
	try:
		c = Calendar( 1, 2, 999)
	except:
		pass
	try:
		c = Calendar( 1, 2, 3000 )
	except:
		pass