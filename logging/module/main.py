#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging, sys

print('getting rootLogger')
# get rootlogger
rootlogger = logging.getLogger()
rootlogger.setLevel(logging.DEBUG)

print( 'rootLogger.getEffectiveLevel number: ', rootlogger.getEffectiveLevel())
print( 'rootLogger.getEffectiveLevel name: ', logging.getLevelName(rootlogger.getEffectiveLevel()))

for level in sorted(logging._levelToName):
	print( 'rootLogger.isEnabledFor: ',  logging._levelToName[level], rootlogger.isEnabledFor(level) )


logging.debug		('logging::debug')
logging.info		('logging::info')
logging.warn		('logging::warn')
logging.error		('logging::error')
logging.critical	('logging::critical')

rootlogger.debug	('root::debug')
rootlogger.info		('root::info')
rootlogger.warn		('root::warn')
rootlogger.error	('root::error')
rootlogger.critical	('root::critical')


sys.exit()

# create logger
mainlogger = logging.getLogger('main')
mainlogger.setLevel(logging.DEBUG)

# create console handler and set level to DEBUG
fh = logging.FileHandler('main.log', mode='w')
fh.setLevel(logging.DEBUG)

# create console handler and set level to DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter
mainFileFormatter = logging.Formatter(
									  '[MAIN:file   ] '
									+ '%(asctime)s'
									+ ' - '
									+ '%(name)s'		# simple_example
									+ ' - '
									+ '%(levelname)s'
									+ ' - '
									+ '%(message)s'
							)

# create formatter
mainConsoleFormatter = logging.Formatter(
									  '[MAIN:console] '
									+ '%(asctime)s'
									+ ' - '
									+ '%(name)s'		# simple_example
									+ ' - '
									+ '%(levelname)s'
									+ ' - '
									+ '%(message)s'
							)

# add formatter to ch
ch.setFormatter(mainConsoleFormatter)
fh.setFormatter(mainFileFormatter)

# add ch to logger
mainlogger.addHandler(ch)
mainlogger.addHandler(fh)


import lib.module as m

rootlogger.debug	('root:debug')
rootlogger.info		('root:info')
rootlogger.warn		('root:warn')
rootlogger.error	('root:error')
rootlogger.critical	('root:critical')

mainlogger.debug	('main:debug')
mainlogger.info		('main:info')
mainlogger.warn		('main:warn')
mainlogger.error	('main:error')
mainlogger.critical	('main:critical')

x = m.Moduleclass()
x.method()
m.fn()

