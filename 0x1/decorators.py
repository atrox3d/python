#!/usr/bin/env python3
import logging, re
#
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s | %(module)s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
log = logging.getLogger(__name__) 
print("################################################################################")
print("#                                                                              #")
print("#    passing function as arguments                                             #")
print("#                                                                              #")
print("################################################################################")
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
print("################################################################################")
print("#                                                                              #")
print("#    returning functions                                                       #")
print("#                                                                              #")
print("################################################################################")
def external(extparam):

	def otherinternal():
		print("otherinternal here")
	#
	#	define ad internal function
	#	extparam is "saved" into internal scope
	#
	externalscopevar = "scope:externalscopevar"
	def internal(
					intparam, 								# will be passed when calling internal
					extargument=extparam					# another way to persist
		):
		#
		#	extparam value is accessed from internal scope
		#	externalscopevar is accessed from internal scope
		#	extargument saves extparam in a local variable
		#
		print( "externalscopevar : ", externalscopevar )
		print( "str(extparam)    : ", str(extparam)    )
		print( "extargument      : ", extargument      )
		print( "str(intparam)    : ", str(intparam)    )
		
		otherinternal()
	#
	#	return the function
	#
	return internal, otherinternal
	

try:
	internal()
except Exception as e:
	print(e)

f, g =external("external param")
print("f.__name__       : ", f.__name__)

f("internal param")
g()




