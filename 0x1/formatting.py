#!/usr/bin/env python3
import logging
import random
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s | %(module)-15s | %(name)-10s:%(funcName)-10s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
log = logging.getLogger(__name__) 

def getline(width=50):
	return "#"*width

def logbanner( message, linewidth=50, logfunc=log.info,  ):
	logfunc(getline())
	logfunc(message)
	logfunc(getline())

logbanner(
	"FLOATS",
	#logfunc=log.debug
)

floats = [ x * random.random() for x in range(0, 50, 5) ]
for f in floats:
	log.info("%-6s %%6.2f	: %6.2f", "float", f )

logbanner(
	"HEX",
	#logfunc=log.debug
)

width=10

log.info("%-*s %%-6x	: %-6x"  , width, "hex", 42 )
log.info("%-*s %%-#6x	: %-#6x" , width, "hex", 42 )
log.info("%-*s %%#6x	: %#6x"  , width, "hex", 42 )
log.info("%-*s %%#6x	: %#6x"  , width, "hex", 42 )
log.info("%-*s %%#6X	: %#6X"  , width, "hex", 42 )
log.info("%-*s %%#6.6x	: %#6.6x", width, "hex", 42 )
log.info(getline())
