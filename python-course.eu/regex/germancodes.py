#!/usr/bin/env python3
""" https://www.python-course.eu/python3_re.php """
import re
from urllib.request import urlopen
import logging
import sys
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	format	= 	"%(asctime)s | " + 
				#"%(module)-15s | " + 
				#"%(name)-10s:%(funcName)-10s | " + 
				"%(levelname)-" + 
				str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S'
	)
#
log = logging.getLogger(__name__) 

url='https://www.python-course.eu/post_codes_germany.txt'
urlfile =  url.split('/')[-1]
with urlopen(url) as gc:							# 	open online resource
	charset=gc.info().get_content_charset()     	#	get charset
	
	citycodes = {}									#	codes dict
	
	for line in gc:                             	#	loop over content
		log.debug(
					"%s : %s",
					urlfile,
					line.decode(charset).rstrip()	#	decode every line
				)
		#mo = re.search(
		#				r"[\d ]+"
		#			#+	r"([^\d]+[a-z])"			# fails with german chars
		#			+	r"([^\d\s]+)"
		#			+	r"\s+"
		#			+	r"(\d+)"
		#			,
		#			line.decode(charset).rstrip()
		#		)
				
		mo = re.search(
						r'''
						[\d ]+
						# ([^\d]+[a-z])"			# fails with german chars
						([^\d\s]+)
						\s+
						(\d+)
						'''
					,
					line.decode(charset).rstrip(),
					re.VERBOSE
				)
				
		if mo: 
			log.debug("'%s', %s", mo.group(), mo.groups())
			city, postcode = mo.groups()
			if city in citycodes:
				citycodes[city].add(postcode)
			else:
				citycodes[city] = {postcode}

localfile='german.population.txt'				
with open(localfile) as gp:							# 	open data file
	for line in gp:                             	#	loop over content
		log.debug(
					"%s : %s",
					localfile,
					line.rstrip()					
				)

