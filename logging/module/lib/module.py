#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

# create logger
modulelogger = logging.getLogger('main.module')

modulelogger.info		(	'%s::loading START ***',	__name__)

modulelogger.debug		(	'%s::debug',	__name__)
modulelogger.info		(	'%s::info',		__name__)
modulelogger.warn		(	'%s::warn',		__name__)
modulelogger.error		(	'%s::error',	__name__)
modulelogger.critical	(	'%s::critical',	__name__)

class	Moduleclass:
	def __init__(self):
		self.logger = logging.getLogger('main.module.moduleclass')
		self.logger.info('Moduleclass.__init__()')

	def method(self):
		self.logger.info('Moduleclass.method()')

def fn():
	modulelogger.info('module.fn()')

modulelogger.info		(	'%s::loading END ***',	__name__)