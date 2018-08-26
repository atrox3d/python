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

width		= 20
format		= "[shellmode:%s] %-{0}.{0}s = %s".format(width)
subformat 	= "	%-{0}.{0}s = %s".format(width)

if __name__ == "__main__":
	for shellmode in [False, True]:
		#
		#	let's try some ls variant
		#
		for command in  [ 
							'ls', 
							'ls *',				
							['ls', '*'],		
							'ls ~', 			
							['ls', '~'],		
							'ls -l',			
							['ls', '-l'],		
							['ls', '-l ~'],		
							['ls', '-l', '~'],	
							'ls -l $HOME', 		
							['ls', '-l', '$HOME'], 
							'echo $(ls  ~)', 	
							'env',				
						]:
			#
			#	log the command being executed
			#
			log.info('--------------------------------------------------------------')
			log.info(format, shellmode, 'command', command)
			log.info('--------------------------------------------------------------')
			#
			#	capture command output
			#
			try:
				process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = shellmode)
				process.wait()
				
				log.info(format, shellmode, 'process.returncode', process.returncode)
				
				#if process.returncode == 0:
				#log.info(format, 'process.stdin', process.stdin)
				log.info(format, shellmode, 'process.stdout', process.stdout)
				#else:
				log.info(format, shellmode, 'process.stderr', process.stderr)
				
				for line in process.stdout:
					log.info(line.decode().rstrip())
				
				for line in process.stderr:
					log.error(line.decode().rstrip())
			except Exception as e:
				log.fatal(e)
			
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
		
	
