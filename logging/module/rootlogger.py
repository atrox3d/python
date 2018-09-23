#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging, sys

def HR():
	print('-' * 80)
	

HR()
print('getting rootLogger, setting to DEBUG')
# get rootlogger
rootlogger = logging.getLogger()
rootlogger.setLevel(logging.DEBUG)

HR()
print('display rootLogger levels')
HR()
print( 'rootLogger.getEffectiveLevel number: ', rootlogger.getEffectiveLevel())
print( 'rootLogger.getEffectiveLevel name: ', logging.getLevelName(rootlogger.getEffectiveLevel()))

for level in sorted(logging._levelToName):
	print( 'rootLogger.isEnabledFor: ',  logging._levelToName[level], rootlogger.isEnabledFor(level) )

HR()
print('rootlogger.hasHandlers : ', rootlogger.hasHandlers())

HR()
print('logging.BASIC_FORMAT : ', logging.BASIC_FORMAT)
print('logging.basicConfig : format=', 'FIRST %(levelname)s:%(name)s:%(message)s')
logging.basicConfig(format='FIRST %(levelname)s:%(name)s:%(message)s')
print('logging.BASIC_FORMAT : ', logging.BASIC_FORMAT)

HR()
print('rootlogger.hasHandlers : ', rootlogger.hasHandlers())
	
HR()
print('use logging')
HR()
logging.debug		('[logging] debug')
logging.info		('[logging] info')
logging.warn		('[logging] warn')
logging.error		('[logging] error')
logging.critical	('[logging] critical')

HR()
print('use rootlogger')
HR()
rootlogger.debug	('[root] debug')
rootlogger.info		('[root] info')
rootlogger.warn		('[root] warn')
rootlogger.error	('[root] error')
rootlogger.critical	('[root] critical')

#
# this will have no effect
#
HR()
print()
print()
print('try to configure root logger without success because hasHandlers=TRUE')
print()
print()
HR()
print('logging.BASIC_FORMAT : ', logging.BASIC_FORMAT)
print('logging.basicConfig : format=', 'hello %(levelname)s:%(name)s:%(message)s')
logging.basicConfig(format='SECOND %(levelname)s:%(name)s:%(message)s')
print('logging.BASIC_FORMAT : ', logging.BASIC_FORMAT)

HR()
print('rootlogger.setLevel(logging.ERROR) works on both logging and rootlogger')
rootlogger.setLevel(logging.ERROR)

HR()
logging.debug		('[logging] debug')
logging.info		('[logging] info')
logging.warn		('[logging] warn')
logging.error		('[logging] error')
logging.critical	('[logging] critical')

HR()
rootlogger.debug	('[root] debug')
rootlogger.info		('[root] info')
rootlogger.warn		('[root] warn')
rootlogger.error	('[root] error')
rootlogger.critical	('[root] critical')
