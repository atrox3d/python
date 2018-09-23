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


