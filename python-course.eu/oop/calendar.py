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
		log.debug("%-10.10s = %s", 'year', year)

		if not year % 4 == 0: 
			log.debug("year %s is not leap, not divisible by 4", year)
			return False
		elif not year % 100 == 0: 
			log.debug("year %s is not leap, not divisible by 100", year)
			return False
		elif not year % 400 == 0: 
			log.debug("year %s is not leap, not divisible by 400", year)
			return False
		else: 
			log.debug("year %s is leap", year)
			return True
	
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
		
	def advance(self):
		"""
		"""
		maxdays = Calendar.months[self.__month - 1]
		log.debug("%-10.10s = %s", 'maxdays', maxdays)
		
		if self.__month == 2:
			leap = Calendar.leapyear(self.__year)
			log.debug("%-10.10s = %s", 'leap', leap)
			
			if leap:
				maxdays += 1
				log.debug("%-10.10s = %s", 'maxdays', maxdays)
				
		if self.__day == maxdays:
			self.__day = 1
			if self.__month == 12:
				self.__month = 1
				self.__year += 1
			else:
				self.__month += 1
		else:
			self.__day += 1
		log.debug("%-10.10s = %s", '__str__', self.__str__())
	
		

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
	
	c = Calendar( 31, 12, 3000 )
	c.advance()
	