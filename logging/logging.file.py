#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logging.debug("this message should go to the log file")
logging.info('so should this')
logging.warning('and this too')

