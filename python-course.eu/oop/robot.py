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
	pass

if __name__ == "__main__":
	#
	#	class attribute
	#
	Robot.attr1 =  "Robot class's attribute"
	#
	#	some class info
	#
	log.info("Robot    : %s", Robot)
	for d in filter(lambda x: not x.startswith("__"), dir(Robot)):
		log.info("	contents : %s", d     )
	log.info("attr1     : %s", Robot.attr1     )
	log.info("__dict__ : %s", Robot.__dict__ )
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
			log.info("	contents : %s", d     )
		log.info("attr1     : %s", r.attr1     )
		log.info("__dict__ : %s", r.__dict__ )

