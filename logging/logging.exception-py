#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

# the default level is warning so only the first line will be printed
logging.basicConfig(level=logging.INFO)
logging.info('START')
logging.warning('watch out for the next exception')
try:
	open("nonexistent.file")
except Exception as e:
	logging.error("here goes the error")
	logging.exception("here goes the exception")
logging.info('END')

