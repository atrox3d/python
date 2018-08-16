#!/usr/bin/env python3
import logging
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	"%(asctime)s | " + 
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
class Robot:
	def __init__(self, name = 'Nameless'):
		#self.name = name
		self.setname(name)
		
		self.public = 'public'
		self._protected = 'protected'
		self.__private = 'private'
		
	
	def hello(self):
		print('hello from ' + self.name)
		
	def setname(self, name):
		self.name = name
		
	def getname(self):
		return self.name
		
	def __repr__(self):
		return "{}('{}')".format(self.__class__.__name__, self.name)

	def __str__(self):
		return "{} : {}".format(self.__class__.__name__, self.name)

if __name__ == "__main__":
	#
	#	class attribute
	#
	Robot.attr1 =  "Robot class's attribute"
	#
	#	some class info
	#
	log.info("Robot    : %s", Robot)
	#for d in filter(lambda x: not x.startswith("__"), dir(Robot)):
	for d in dir(Robot):
		log.info("	contents : %s = %s", d, getattr(Robot,d)     )
	log.info("attr1     : %s", Robot.attr1     )
	log.info("__dict__  : %s", Robot.__dict__ )
	log.info("getattr   : %s", getattr(Robot, 'attr1' ))
	log.info("repr      : %s", repr(Robot))
	log.info("str       : %s", str(Robot))
	log.info("------------------------------------------------------------------")
	#
	#	two instances
	#
	r2d2 = Robot()
	c3po = Robot()
	#
	#	instance attribute
	#
	r2d2.attr1 = "r2d2 instance's attribute"
	c3po.attr1 = "c3po instance's attribute"
	#
	#	loop over instances
	#
	for r in [ r2d2, c3po ]:
		log.info("robot    : %s", r          )
		for d in filter(lambda x: not x.startswith("__"), dir(r)):
			log.info("	contents : %s = %s ", d, getattr(r,d )     )
		log.info("attr1        : %s", r.attr1     )
		log.info("__dict__     : %s", r.__dict__ )
		log.info("getattr      : %s", getattr(r, 'attr1' ))
		log.info("repr         : %s", repr(r))
		log.info("str          : %s", str(r))
		r.hello()
		log.info("r.public     : %s", r.public)
		log.info("r._protected : %s", r._protected)
		try:
			log.info("r.__private  : %s", r.__private)
		except Exception as e:
			log.error(e)
		log.info("------------------------------------------------------------------")

