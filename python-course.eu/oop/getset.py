#!/usr/bin/env python3
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
class P:
	def __init__(self, x, y):
		log.debug("x = %s, y = %s", x, y)
		self.x = x
		self.y = y
		
	@property
	def x(self):
		log.debug("return x = %s", self.__x )
		return self.__x
		
	@x.setter
	def x(self, x):
		log.debug("set x = %s", x )
		self.__x = x
		
	def sety(self, y):
		log.debug("set y = %s", y )
		self.__y = y
		
	def gety(self):
		log.debug("return y = %s", self.__y )
		return self.__y
	
	y = property(gety, sety)

if __name__ == "__main__":
	p = P(1, 2)
	
	log.info("p.x = %s", p.x)
	log.info("p.y = %s", p.y)
	