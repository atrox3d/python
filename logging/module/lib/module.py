#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

# create console handler and set level to DEBUG
fh = logging.FileHandler('module.log', mode='w')
fh.setLevel(logging.DEBUG)

# create formatter
moduleFileFormatter = logging.Formatter(
									  '[moduleFileFormatter] '
									+ '%(asctime)s'
									+ ' - '
									+ '%(name)s'		# simple_example
									+ ' - '
									+ '%(levelname)s'
									+ ' - '
									+ '%(message)s'
							)

fh.setFormatter(moduleFileFormatter)

# create logger
modulelogger = logging.getLogger('main.module')

modulelogger.addHandler(fh)
#modulelogger.propagate=False

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