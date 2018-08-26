#!/usr/bin/env python3
"""

"""

import logging, subprocess, sys
#
logging.basicConfig(
	#level	= 	logging.DEBUG,
	level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				#"%(module)-15.15s | " + 
				#"%(name)-10s:" +
				#"%(funcName)-15.15s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	) #
log=logging.getLogger(__name__)

format     = "%-{0}.{0}s = %s".format(30)
subformat  = "	%-{0}.{0}s = %s".format(30)

if __name__ == "__main__":
	#
	#	let's try some ls variant
	#
	for command in  [ 
						'ls', 
						#'ls *',				# globbing
						#'ls ~', 
						#'ls -l', 
						#'ls -l ~', 
						#'ls -l $HOME', 		# environment expansion
						#'echo $(ls  ~)', 	# command substitution/subshell
						#'env',
					]:
		#
		#	log the command being executed
		#
		log.info('--------------------------------------------------------------')
		log.info(command)
		log.info('--------------------------------------------------------------')
		#
		#	capture command output
		#
		try:
			process = subprocess.Popen(command, stdout = subprocess.PIPE)
			process.wait()
			log.info(format, 'returncode', process.returncode)
			#for item in dir(process):
			#	print(item)
			#lines = process.readlines()
			#for line  in lines:
			#	log.info(line.rstrip())
		except Exception as e:
			log.error(e)
			
	sys.exit(0)
	#
	#	let's work with output
	#
	command = 'ls -la ~'
	log.info('--------------------------------------------------------------')
	log.info(command)
	log.info('--------------------------------------------------------------')
	try:
		process = os.popen(command)
		lines = process.readlines()
		for entry  in lines:
			#
			#	split each line at whitespace
			#
			listfields = entry.split()
			log.debug(listfields)
			try:
				#
				#	try the normal ls -l format
				#	*extra captures extra fields
				#
				attributes, number, user, group, size, month, day, time, name, *extra = listfields
				#	dir
				if attributes.startswith("d"):
					log.info("DIR  %s/", name)
				# file
				elif attributes.startswith("-"):
					log.info("FILE %s", name)
				# link
				elif attributes.startswith("l"):
					log.info("LINK %s", name)
				# dk/dc
				else:
					log.info("???? %s", name)
			except Exception as e:
				#
				#	usually total xxx
				#
				log.error(e)
				log.error(listfields)
	except Exception as e:
		log.error(e)
		
	
