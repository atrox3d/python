#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simple_example')

logger.debug('debug')
logger.info('info')
logger.warn('warn')
logger.error('error')
logger.critical('critical')