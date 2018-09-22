#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging, sys

# create logger
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# create console handler and set level to DEBUG
fh = logging.FileHandler('main.log', mode='w')
fh.setLevel(logging.DEBUG)

# create console handler and set level to DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

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
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


import lib.module as m

logger.debug('debug')
logger.info('info')
logger.warn('warn')
logger.error('error')
logger.critical('critical')

x = m.Moduleclass()
x.method()
m.fn()

