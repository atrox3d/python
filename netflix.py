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

def regexline(regex,line):
	""" return rexex result as mo.groups() """
	chunkregex = re.compile(regex)
	mo = chunkregex.search(line)
	if mo:
		log.debug("mo.group    %s", mo.group())
		log.debug("mo.groups   %s", mo.groups())
		return mo.groups()
	else:
		log.error("no mo.group for '%s' in '%s'", regex, line)



netflixlog=open('private/netflix.log')					# open log file

header=netflixlog.readline()							# read header
log.info(header.rstrip())								# displaye header

lineno=-1												# init counter
buffer=[]												# init temp buffer
record={}                                               # my little db
fields=()                                               # mo.group()
stats=set()                                             # aggregation set
#
for line in netflixlog:									# loop over file: read line
	line = line.rstrip()								# get rid of \n
	lineno += 1											# count lines
	linemod=lineno%3									# count groups of 3 lines
	buffer.append(line)									# add to line buffer
	#
	#	every line is broken in three sublines because of copy/paste
	#
	if   linemod == 0:									# get 1st   group: date/time
		#
		#	the 1st of 3 has date and time GMT+1
		#
		regex=r"(\d\d/\d\d/\d\d),\s+(\d\d:\d\d:\d\d)\s+(GMT\+1)"
		date = time = timezone = None
		fields = regexline(regex, line)
		#
		#	if regex succeded we save the resulting fields into our temp record
		#
		if fields:
			date, time, timezone = fields
			log.debug("date: %s, time: %s, timezone: %s", date, time, timezone)
			record['date'] = date
			record['time'] = time
			record['timezone'] = timezone
		
	elif linemod == 1:									# get 2nd   group: location
		#
		#	the 2nd line has "Italia" and (city abbreviation)
		#
		regex=r"(Italia)\s+\(([A-Z]+)\)"
		fields = regexline(regex, line)
		#
		#	if regex succeded we save the resulting fields into our temp record
		#
		if fields:
			nation, city= fields
			log.debug("nation: %s, city: %s", nation, city)
			record['nation'] = nation
			record['city'] = city
		
	elif linemod == 2:									# get last  group: ip devicename
		#
		#	the 3d line has ip address and evice name
		#
		regex=r"(\d+\.\d+\.\d+\.\d+)\s+(.+)"
		fields = regexline(regex, line)
		#
		#	if regex succeded we save the resulting fields into our temp record
		#
		if fields:
			ip, device= fields
			log.debug("ip: %s, device: %s", ip, device)
			record['ip'] = ip
			record['device'] = device
			log.debug(record)
		#################################################
		# join buffer into whole line
		#################################################
		#
		#	just for logging
		#
		#
		joinchar=" | "									# join char
		wholeline = joinchar.join(buffer)				# join line
		#
		#	if all regex succeded we save the important information
		#	we use a set, so that double records get deleted
		#
		if len(record) == 7:
			stats.add( 
						(
								record['ip'], 
								record['city'], 
								record['device'],
								record['date']
							) 
						)
		#if fields:
			for k, v in record.items():
				log.info("%-15s : %s", k, v)
		else:
			#
			#	if some regex fails, we print the whole line
			#
			log.info(wholeline)								# display whole line
			
		buffer=[]										# reinitialize buffer
		record={}										# reinitialize temp record
	else:
		log.error("[%d]	%s", linemod, line)				# something's wrong
		continue

report={}												# final db
#
#	final report
#
for ip, city, device, date in stats:					# loop over stats and extract data
	#
	if ip in report.keys():								# already added?
		if city in report[ip].keys():					# already added?
			if device not in report[ip][city]:			# if not already done
				report[ip][city].append(device)			# append another device 
		else:
			report[ip][city] = device					# add device
	else:
		report[ip] = { city : [device] }				# create first entry
#
#
#
print("-" * 80 )
print( "%18s, %-10s, %s" % ("ip address", "city", "dispositivi") )
print("-" * 80 )
#
for ip in sorted(report.keys()):						# loop over sorted ips
	rec = report[ip]									# extract record for ip
	for city in rec.keys():								# print remaining data
		log.debug("%18s, %s, %s", ip, city, rec[city])
		print("%18s, %-10s, %s" % ( ip, city, rec[city]))
		pass
		
		
		
		
		
		
