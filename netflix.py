#!/usr/bin/env python3
import logging
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
netflixlog=open('netflix.log')							# open log file

header=netflixlog.readline()							# read header
log.info(header.rstrip())								# displaye header

lineno=-1												# init counter
buffer=[]												# init temp buffer

for line in netflixlog:									# loop over file: read line
	line = line.rstrip()								# get rid of \n
	lineno += 1											# count lines
	linemod=lineno%3									# count groups of 3 lines
	buffer.append(line)									# add to line buffer
	
	if   linemod == 0:									# get 1st   group: date/time
		pass
	elif linemod == 1:									# get 2nd   group: location
		pass
	elif linemod == 2:									# get last  group: ip devicename
		log.debug("[%d]	%s", linemod, line)
		
		# regex (ip.address)\s+(.+)
		
		joinchar=" | "									# join char
		wholeline = joinchar.join(buffer)				# join line
		log.info(wholeline)								# display whole line
		buffer=[]										# reinitialize buffer
	else:
		log.error("[%d]	%s", linemod, line)


