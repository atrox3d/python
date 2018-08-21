#!/usr/bin/env python3
import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
log=logging.getLogger(__name__) 

#
#	logvar (experimental)
#
#	compare var address (id) to print name and value
#
def logvar(name):
	for k in globals():
		if id(name) == id(globals()[k]):
			log.debug("%-20.20s: %s", k, globals()[k])
			break
	else:
		log.error("%-20.20s: %s", name, "UNDEFINED")

#
#	debugvar (experimental)
#
#	compare var address (id) to print name and info
#
def debugvar(name, printdir=False):
	for k in globals():
		if id(name) == id(globals()[k]):
			log.debug("%-20.20s: [%-5.5s] %s", k, "-" * 5 , "-" * 50)
			log.debug("%-20.20s: [%-5.5s] %s", k, "VALUE", globals()[k])
			log.debug("%-20.20s: [%-5.5s] %s", k, "STR",   str (globals()[k]))
			log.debug("%-20.20s: [%-5.5s] %s", k, "TYPE",  type(globals()[k]))
			log.debug("%-20.20s: [%-5.5s] %s", k, "REPR",  repr(globals()[k]))
			if printdir:
				log.debug("%-20.20s: [%-5.5s] %s", k, "-" * 5 , "{")
				for d in dir (globals()[k]):
					if not d.startswith('__'):
						log.debug("%-20.20s: [%-5.5s] 		%s", k, "DIR",  d )
				log.debug("%-20.20s: [%-5.5s] %s", k, "-" * 5 , "}")
			break
	else:
		log.error("%-20.20s: %s", name, "UNDEFINED")

#
#	import regex package
#
import re
#
#	create regex object
#
#	r'string' : raw string (no escape interpretation, otherwise \\d)
#
regex = r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
debugvar(regex)
#
phoneNumberRegex =  re.compile(regex)
debugvar(phoneNumberRegex, True)
#
#	search text against regex
#
mo = phoneNumberRegex.search('My number is 415-555-4242.')
debugvar(mo, True)
#
#	two different string interpolation methods
#
#print("mo.group    %s" % mo.group())
log.debug("mo.group    %s" % mo.group())
print("mo.group    {}".format(mo.group()))
#
#	print tuple
#
print("mo.groups   {}".format(mo.groups()))
#
#	play with tuple
#
for group in mo.groups():
	print("mo.group    %5.5s" % group)
#
#	play with string format
#
for i in range(len(mo.groups())+1):
	print("group %d	%20.20s" % (i, mo.group(i)))
	print("group {}	{:>20s}".format( i, mo.group(i)))
#
# multi assignment
#
a, b, c = mo.groups()
#
#	keyword formatting
#
print( "a={}, b={}, c={c}".format( a, b, c=c ))
#
#	print result
#
print('\nPhone number found: ' + mo.group())
