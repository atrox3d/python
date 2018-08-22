#!/usr/bin/env python3
"""

"""

import logging, os, sys
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
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

format     = "sys.%-{0}.{0}s = %s".format(30)
subformat  = "	sys.%-{0}.{0}s = %s".format(30)

if __name__ == "__main__":
	#
	#	let's try some ls variant
	#
	for command in  [ 
						'ls', 
						'ls *',				# globbing
						'ls ~', 
						'ls -l', 
						'ls -l ~', 
						'ls -l $HOME', 		# environment expansion
						'echo $(ls  ~)', 	# command substitution/subshell
						'env',
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
			process = os.popen(command)
			lines = process.readlines()
			for entry  in lines:
				log.info(entry.rstrip())
		except Exception as e:
			log.error(e)
