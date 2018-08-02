#!/usr/bin/env python3
import logging
import random
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s | %(module)-15s | %(name)-10s:%(funcName)s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
log = logging.getLogger(__name__) 

log.info("start")
floats = [ x * random.random() for x in range(0, 100, 5) ]
for f in floats:
	log.info("%%6.2f	: %6.2f", f )

