#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

# the default level is warning so only the first line will be printed
#logging.basicConfig(level=logging.INFO)
def hello():
	logging.info('this is %s logging', __name__)
