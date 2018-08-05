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
#	passing function as arguments
#
def functioncaller(f):
	print("calling " + f.__name__)
	f()
#
#	define some functions
#
def f1():	print("f1 here")
def f2():	print("f2 here")
def f3():	print("f3 here")
def f4():	print("f4 here")
#
#	list of functions
#
fx = [ f1, f2, f3, f4 ]
#
#	loop call functions
#
for f in fx:
	functioncaller(f)

