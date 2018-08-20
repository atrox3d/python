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
debug_value_format = "%-{0}.{0}s : %s".format(15)
class Validator:
	def __init__(self, value, *validators):

		self.value = value

		self.validators = []
		for validator in validators:
			self.validators.append(validator)

		log.debug(debug_value_format,  'value',			value)
		log.debug(debug_value_format,  'validators',		validators)
		log.debug(debug_value_format,  'self.value',		self.value)
		log.debug(debug_value_format,  'self.validators',	self.validators)
	
	#def add(self, validatorfunc):
	#	self.__validators.append(validatorfunc)
		
	def isvalid():
		pass


#def validator(value, *valfuncs):
#	for v in valfuncs:
#		if not v(value):
#			return False
#	
#	return True


if __name__ == "__main__":
	v = Validator(5)