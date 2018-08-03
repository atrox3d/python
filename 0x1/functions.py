#!/usr/bin/env python3

import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s | %(module)-15s | %(name)-10s:%(funcName)s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#

log = logging.getLogger(__name__) 

def getline(width=50, char="#"):
	return char*width

def logbanner( message, linewidth=50, logfunc=log.info,  char="#"):
	logfunc(getline(linewidth,char=char))
	logfunc(message)
	logfunc(getline(linewidth,char))


def afunction(aparameter="default parameter value"):
	""" prints the parameter"""
	print("afunction(%s)" % aparameter)

log.info("afunction()	: %s", afunction.__doc__)
afunction()


def multiplereturn(aint=0):
	return (aint, aint+1)
	
log.info("aint()	= %s", multiplereturn())
log.info("aint()	= %d, %d", *multiplereturn())
