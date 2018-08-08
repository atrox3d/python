#!/usr/bin/env python3
""" https://www.python-course.eu/python3_re.php """
import re
from urllib.request import urlopen
import logging
import sys
#
logging.basicConfig(
	level	= 	logging.INFO,
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
	cities = set()
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
				
			cities.add(city)
		else:
			log.warning("regexp FAIL")
			log.warning(line.decode(charset).rstrip())

				
			
localfile='german.population.txt'				
with open(localfile, encoding="utf-8") as gp:							# 	open data file
	for line in gp:                             	#	loop over content
		log.debug(
					"%s : %s",
					localfile,
					line.rstrip()					
				)

		mo = re.search(
						r'''
						^[0-9]{1,2}\.
						\s+
						([\w\s-]+\w)
						\s+
						[0-9]
						
						'''
					,
					line.rstrip(),
					re.VERBOSE
				)

		if mo: 
			log.debug("'%s', %s", mo.group(), mo.groups())
			city=mo.groups(1)
			
			if city in citycodes:
				print(city, citycodes[city])
			#else:
			#	log.error("city %s not found", city)
			if city in cities:
				log.info("%s found in cities", city)
			else:
				log.warning("%s not found in cities", city)
			

