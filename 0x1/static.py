#!/usr/bin/env python3
def static(f):
	def wrapper():
		staticval=0
		print("before %s: staticval = %d" % (f.__name__, staticval))
		f()
		print("after %s: staticval = %d" % (f.__name__, staticval))
	 
	return wrapper

@static
def f():
	staticval += 1

f()
