#!/usr/bin/env python3
import logging, re
#
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s | %(module)s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
log = logging.getLogger(__name__) 
#
#
#
def functioncaller(f):
	param="hello"
	f(param)

def function(x):
	print(x)

functioncaller(function)
