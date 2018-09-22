#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
								  '%(asctime)s'
								+ ' - '
								+ '%(name)s'		# simple_example
								+ ' - '
								+ '%(levelname)s'
								+ ' - '
								+ '%(message)s'
							)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

logger.debug('debug')
logger.info('info')
logger.warn('warn')
logger.error('error')
logger.critical('critical')