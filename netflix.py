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
	chunkregex = re.compile(regex)
	mo = chunkregex.search(line)
	if mo:
		log.debug("mo.group    %s", mo.group())
		log.debug("mo.groups   %s", mo.groups())
		return mo.groups()
	else:
		log.error("no mo.group for '%s' in '%s'", regex, line)



netflixlog=open('private/netflix.log')							# open log file

header=netflixlog.readline()							# read header
log.info(header.rstrip())								# displaye header

lineno=-1												# init counter
buffer=[]												# init temp buffer
record={}
fields=()
stats=set()
for line in netflixlog:									# loop over file: read line
	line = line.rstrip()								# get rid of \n
	lineno += 1											# count lines
	linemod=lineno%3									# count groups of 3 lines
	buffer.append(line)									# add to line buffer
	#log.debug("[%d]	%s", linemod, line)
	if   linemod == 0:									# get 1st   group: date/time
		
		regex=r"(\d\d/\d\d/\d\d),\s+(\d\d:\d\d:\d\d)\s+(GMT\+1)"
		data = ora = fuso = None
		fields = regexline(regex, line)
		if fields:
			data, ora, fuso = fields
			log.debug("data: %s, ora: %s, fuso: %s", data, ora, fuso)
			record['data'] = data
			record['ora'] = ora
			record['fuso'] = fuso
		
	elif linemod == 1:									# get 2nd   group: location
		
		regex=r"(Italia)\s+\(([A-Z]+)\)"
		fields = regexline(regex, line)
		if fields:
			nazione, provincia= fields
			log.debug("nazione: %s, provincia: %s", nazione, provincia)
			record['nazione'] = nazione
			record['provincia'] = provincia
		
	elif linemod == 2:									# get last  group: ip devicename
		
		regex=r"(\d+\.\d+\.\d+\.\d+)\s+(.+)"
		fields = regexline(regex, line)
		if fields:
			ip, device= fields
			log.debug("ip: %s, device: %s", ip, device)
			record['ip'] = ip
			record['device'] = device
			log.debug(record)
			stats.add( 
						(
								record['ip'], 
								record['provincia'], 
								record['device']
							) 
						)
		#################################################
		# join buffer into whole line
		#################################################
		joinchar=" | "									# join char
		wholeline = joinchar.join(buffer)				# join line
		
		if fields:
			for k, v in record.items():
				log.info("%-15s : %s", k, v)
		else:
			log.info(wholeline)								# display whole line
			
		buffer=[]										# reinitialize buffer
		record={}										# reinitialize buffer
	else:
		log.error("[%d]	%s", linemod, line)
		continue

report={}
for ip, provincia, device in stats:
	if ip in report.keys():
		if provincia in report[ip].keys():
			if device not in report[ip][provincia]:
				report[ip][provincia].append(device)
		else:
			report[ip][provincia] = device
	else:
		report[ip] = { provincia : [device] }
		
for ip in sorted(report.keys()):
	print(ip)
	
for ip, rec in report.items():
	for provincia in rec.keys():
		log.info("%18s, %s, %s", ip, provincia, rec[provincia])
		pass
		
		
		
		
		
		
