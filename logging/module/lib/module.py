#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

# create logger
modulelogger = logging.getLogger('main.module')

modulelogger.info		(	'loading %s',	__name__)
modulelogger.debug		(	'debug %s',		__name__)
modulelogger.info		(	'info %s',		__name__)
modulelogger.warn		(	'warn %s',		__name__)
modulelogger.error		(	'error %s',		__name__)
modulelogger.critical	(	'critical %s',	__name__)

class	Moduleclass:
	def __init__(self):
		self.logger = logging.getLogger('main.module.moduleclass')
		self.logger.info('init moduleclass')

	def method(self):
		self.logger.info('module.method')

def fn():
	modulelogger.info('module.fn')
